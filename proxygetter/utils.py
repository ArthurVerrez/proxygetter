from typing import List, Dict, Union, Optional
import requests
from bs4 import BeautifulSoup
import re


def parse_time_to_seconds(time_string: str) -> Optional[int]:
    """
    Convert a time string to time in seconds.

    Args:
        time_string (str): Time string in human-readable format, e.g., '15 secs ago'.

    Returns:
        Optional[int]: Time in seconds. Returns 0 for any invalid string format.
    """
    try:
        total_seconds = 0
        for value, unit in re.findall(r"(\d+) (\w+)", time_string):
            value = int(value)

            if "sec" in unit:
                total_seconds += value
            elif "min" in unit:
                total_seconds += value * 60
            elif "hour" in unit:
                total_seconds += value * 3600
            elif "day" in unit:
                total_seconds += value * 86400

        return total_seconds
    except:
        return None


def scrap_sslproxies() -> List[Dict[str, Union[str, bool, int]]]:
    URL = "https://www.sslproxies.org/"
    LINE_SELECTOR = "#list > div > div.table-responsive > div > table > tbody > tr"
    COLUMNS = [
        "ip",
        "port",
        "code",
        "country",
        "anonymity",
        "google",
        "https",
        "last_checked",
    ]
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    lines = soup.select(LINE_SELECTOR)

    return [
        {
            COLUMNS[i]: parse_time_to_seconds(col.text)
            if COLUMNS[i] == "last_checked"
            else (True if col.text == "yes" else False)
            if COLUMNS[i] in ["google", "https"]
            else col.text
            for i, col in enumerate(line.select("td"))
        }
        for line in lines
    ]


def filter_proxies(
    all_proxies: List[Dict[str, Union[str, bool, int]]],
    country_code: Optional[str] = None,
    anonymity: Optional[str] = None,
    https: Optional[bool] = None,
    google: Optional[bool] = None,
    last_checked_max: Optional[int] = None,
) -> List[Dict[str, Union[str, bool, int]]]:
    return [
        proxy
        for proxy in all_proxies
        if all(
            proxy.get(key) == val
            for key, val in {
                "code": country_code,
                "anonymity": anonymity,
                "https": https,
                "google": google,
            }.items()
            if val is not None
        )
        and (
            last_checked_max is None
            or (
                proxy.get("last_checked") is not None
                and proxy["last_checked"] <= last_checked_max
            )
        )
    ]


def get_proxies(
    country_code: Optional[str] = None,
    anonymity: Optional[str] = None,
    https: Optional[bool] = None,
    google: Optional[bool] = None,
    last_checked_max: Optional[int] = None,
) -> List[Dict[str, Union[str, bool, int]]]:
    all_proxies = scrap_sslproxies()
    return filter_proxies(
        all_proxies, country_code, anonymity, https, google, last_checked_max
    )
