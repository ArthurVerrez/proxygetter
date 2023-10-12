from proxygetter.utils import (
    parse_time_to_seconds,
    scrap_sslproxies,
    filter_proxies,
    get_proxies,
)
import requests_mock


def test_parse_time_to_seconds():
    assert parse_time_to_seconds("15 secs ago") == 15
    assert parse_time_to_seconds("1 hour 15 mins ago") == 4500
    assert parse_time_to_seconds("Invalid string") is 0


def test_scrap_sslproxies():
    with open("fake_html.html") as f:
        fake_html = f.read()
    with requests_mock.mock() as m:
        m.get("https://www.sslproxies.org/", text=fake_html)
        proxies = scrap_sslproxies()
        assert len(proxies) > 0
        print(proxies[0])
        assert proxies[0] == {
            "ip": "118.69.111.51",
            "port": "8080",
            "code": "VN",
            "country": "Vietnam",
            "anonymity": "elite proxy",
            "google": False,
            "https": True,
            "last_checked": 19,
        }


def test_filter_proxies():
    proxies = [
        {"code": "US", "anonymity": "elite proxy", "https": True, "google": False},
        {"code": "CA", "anonymity": "medium", "https": False, "google": True},
    ]
    assert filter_proxies(proxies, country_code="US") == [proxies[0]]
    assert filter_proxies(proxies, https=True) == [proxies[0]]
    assert filter_proxies(proxies, https=False, google=True) == [proxies[1]]


def test_get_proxies():
    with open("fake_html.html") as f:
        fake_html = f.read()
    with requests_mock.mock() as m:
        m.get("https://www.sslproxies.org/", text=fake_html)
        proxies = get_proxies(country_code="DE")
        print(proxies[0])
        assert len(proxies) > 0
        assert proxies[0] == {
            "ip": "43.157.8.79",
            "port": "8888",
            "code": "DE",
            "country": "Germany",
            "anonymity": "anonymous",
            "google": True,
            "https": True,
            "last_checked": 600,
        }
