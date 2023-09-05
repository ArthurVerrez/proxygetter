import unittest
from proxygetter.proxygetter import get_proxies, parse_time_to_seconds


class TestProxyGetter(unittest.TestCase):
    def test_parse_time_to_seconds(self):
        self.assertEqual(parse_time_to_seconds("15 secs ago"), 15)
        self.assertEqual(parse_time_to_seconds("1 min ago"), 60)
        self.assertEqual(parse_time_to_seconds("unknown"), 0)

    def test_get_proxies(self):
        proxies = get_proxies()
        self.assertIsInstance(proxies, list)
        self.assertGreater(len(proxies), 0)

        for proxy in proxies:
            self.assertIn("ip", proxy)
            self.assertIn("port", proxy)
            self.assertIn("code", proxy)

    def test_filter_proxies(self):
        us_proxies = get_proxies(country_code="US")
        for proxy in us_proxies:
            self.assertEqual(proxy["code"], "US")

        https_proxies = get_proxies(https=True)
        for proxy in https_proxies:
            self.assertTrue(proxy["https"])


if __name__ == "__main__":
    unittest.main()
