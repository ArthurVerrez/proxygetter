import os

PROXY_URL_CHECKER_USER_AGENT_HEADER = os.getenv(
    "PROXY_URL_CHECKER_USER_AGENT",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
)
PROXY_URL_CHECKER_TIMEOUT = os.getenv("PROXY_URL_CHECKER_TIMEOUT", 5)


class Proxy:
    def __init__(self, proxy_object):
        self.ip = proxy_object["ip"]
        self.port = proxy_object["port"]
        self.anonymity = proxy_object["anonymity"]
        self.country = proxy_object["country"]
        self.country_code = proxy_object["code"]
        self.https = proxy_object["https"]
        self.google = proxy_object["google"]
        self.last_checked = proxy_object["last_checked"]

    def get_requests_format(self):
        return f"http://{self.ip}:{self.port}"

    def get_selenium_format(self):
        return f"{self.ip}:{self.port}"

    def blacklist(self):
        pass

    async def fetch_is_valid(self, session, url):
        """
        Fetch the url with the proxy and check if the status code is 200
        If it is, return the proxy, else return None
        """
        try:
            async with session.get(
                url,
                proxy=self.get_requests_format(),
                headers={"User-Agent": PROXY_URL_CHECKER_USER_AGENT_HEADER},
                timeout=PROXY_URL_CHECKER_TIMEOUT,
            ) as response:
                if response.status == 200:
                    return self
                return None
        except:
            return None

    def __str__(self):
        return self.get_requests_format()

    def __repr__(self):
        return f"{self.ip}:{self.port}, {self.country_code}, {self.anonymity}, {self.https}, {self.google}, {self.last_checked}"
