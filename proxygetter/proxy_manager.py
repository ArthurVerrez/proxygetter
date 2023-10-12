import aiohttp
import asyncio
import nest_asyncio
import random
import os
from .proxy import Proxy
from .utils import get_proxies as utils_get_proxies

PROXY_URL_CHECKER_USER_AGENT_HEADER = os.getenv(
    "PROXY_URL_CHECKER_USER_AGENT",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
)
PROXY_URL_CHECKER_DEFAULT_URL = os.getenv(
    "PROXY_URL_CHECKER_DEFAULT_URL", "http://httpbin.org/ip"
)


class ProxyManager:
    def __init__(self):
        self.proxies = []

    async def filter_with_validity(self, url=PROXY_URL_CHECKER_DEFAULT_URL):
        valid_proxies = []
        async with aiohttp.ClientSession() as session:
            tasks = [proxy.fetch_is_valid(session, url) for proxy in self.proxies]
            for task in asyncio.as_completed(tasks):
                result = await task
                if result:
                    valid_proxies.append(result)

    def get_proxies(
        self,
        anonymity=None,
        country_code=None,
        https=None,
        google=None,
        last_checked_max=None,
        filter_validity_url=PROXY_URL_CHECKER_DEFAULT_URL,
        shuffle=True,
    ):
        """
        Return a list of proxies matching the filters
        """
        self.proxies = [
            Proxy(p)
            for p in utils_get_proxies(
                country_code=country_code,
                anonymity=anonymity,
                https=https,
                google=google,
                last_checked_max=last_checked_max,
            )
        ]
        if shuffle:
            random.shuffle(self.proxies)
        if filter_validity_url:
            nest_asyncio.apply()
            loop = asyncio.get_event_loop()
            if loop.is_closed():
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            loop.run_until_complete(self.filter_with_validity(filter_validity_url))

        return self.proxies

    def get_random_proxy(
        self,
        anonymity=None,
        country_code=None,
        https=None,
        google=None,
        last_checked_max=None,
        filter_validity_url=PROXY_URL_CHECKER_DEFAULT_URL,
        refresh=True,
    ):
        """
        Return a random proxy
        """
        if refresh:
            self.get_proxies(
                anonymity=anonymity,
                country_code=country_code,
                https=https,
                google=google,
                last_checked_max=last_checked_max,
                filter_validity_url=filter_validity_url,
            )
        return random.choice(self.proxies)
