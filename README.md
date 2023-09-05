# proxygetter

## Description

`proxygetter` is a Python utility for scraping and filtering SSL proxies. It is designed to be lightweight, fast, and customizable.

## Installation

You can install `proxygetter` via pip:

```bash
pip install proxygetter
```

## Usage

Here's a quick example of how to use `proxygetter`.

```python
from proxygetter import get_proxies

# Get all available proxies
all_proxies = get_proxies()

# Get proxies from a specific country
us_proxies = get_proxies(country_code='US')

# Get anonymous HTTPS proxies
https_proxies = get_proxies(https=True, anonymity='anonymous')
```

## License

This project is under the MIT License - see the [LICENSE](LICENSE) file for details.

## Tests

You can run the tests using the `unittest` framework with the command:

```bash
python -m unittest tests/test_proxygetter.py
```