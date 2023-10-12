from proxygetter.proxy import Proxy


def create_proxy_object():
    return {
        "ip": "192.168.0.1",
        "port": 8080,
        "anonymity": "elite proxy",
        "country": "USA",
        "code": "US",
        "https": True,
        "google": False,
        "last_checked": "2023-10-12",
    }


def test_init():
    proxy_object = create_proxy_object()
    proxy_instance = Proxy(proxy_object)
    assert proxy_instance.ip == "192.168.0.1"
    assert proxy_instance.port == 8080
    assert proxy_instance.anonymity == "elite proxy"


def test_get_requests_format():
    proxy_object = create_proxy_object()
    proxy_instance = Proxy(proxy_object)
    assert proxy_instance.get_requests_format() == "http://192.168.0.1:8080"


def test_get_selenium_format():
    proxy_object = create_proxy_object()
    proxy_instance = Proxy(proxy_object)
    assert proxy_instance.get_selenium_format() == "192.168.0.1:8080"
