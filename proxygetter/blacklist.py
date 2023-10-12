import os

CACHE_PROXY_BLACKLIST_PATH = os.getenv(
    "CACHE_PROXY_BLACKLIST_PATH", "cache/proxy_blacklist.txt"
)


class Blacklist:
    def __init__(self):
        pass
