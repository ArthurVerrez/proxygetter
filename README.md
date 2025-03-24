# proxygetter

## Description

`proxygetter` is a Python library that provides a fast and customizable way to scrape, filter, and manage proxies. It's powered by asyncio and aiohttp to validate proxies asynchronously. Originally designed to scrape from [sslproxies.org](https://www.sslproxies.org/), it now supports customizable sources and multiple filters.

## Installation

Install the package via pip:

```bash
pip install proxygetter
```

## Features

### Proxy Management

Manage your proxies with ease using the `ProxyManager` class.

```python
from proxygetter import ProxyManager
manager = ProxyManager()
```

### Proxy Information

Access details about each proxy through the `Proxy` class.

```python
proxy = valid_proxies[0]
print(proxy.get_requests_format())
print(proxy.get_selenium_format())
```

### Advanced Filters

Get proxies using advanced filters like country code, anonymity, https support, Google compatibility, and last checked time.

```python
filtered_proxies = manager.get_proxies(country_code='US', anonymity='elite proxy', https=True, google=True, last_checked_max=600)
```

### Fetch a Random Proxy

You can fetch a random proxy based on specified filters.

```python
random_proxy = manager.get_random_proxy(country_code='US', https=True)
```

### Environment Configuration

Configure default user agent and timeout using environment variables.

```bash
export PROXY_URL_CHECKER_USER_AGENT=your_user_agent
export PROXY_URL_CHECKER_TIMEOUT=your_timeout_value
```

## License

This project is under the MIT License - see the [LICENSE](LICENSE) file for details.

## Upcoming Features

- Proxy blacklisting
- Additional proxy databases
- Enhanced documentation and examples

Feel free to contribute or suggest improvements.
