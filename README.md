# proxygetter

## Description

`proxygetter` is a Python utility for scraping and filtering proxies from [sslproxies.org](https://www.sslproxies.org/). It is designed to be lightweight, fast, and customizable.

## Installation

You can install `proxygetter` via pip:

```bash
pip install proxygetter
```

## Usage

### Basic Usage

To get a list of all available proxies:

```python
from proxygetter import get_proxies
proxies = get_proxies()
print(proxies)
```

### Features

#### Filter by Country Code

To get proxies from a specific country:

```python
proxies = get_proxies(country_code='US')
```

#### Filter by Anonymity

To get anonymous or elite proxies (accepted values are `'anonymous'` and `'elite proxy'`):

```python
proxies = get_proxies(anonymity='anonymous')
```

#### Filter by HTTPS support

To get proxies that support HTTPS:

```python
proxies = get_proxies(https=True)
```

#### Filter by Google support

To get proxies that were checked to work with Google:

```python
proxies = get_proxies(google=True)
```

#### Filter by Last Checked Time

To get proxies that were last checked within a certain number of seconds:

```python
proxies = get_proxies(last_checked_max=600)  # Proxies checked within the last 10 minutes
```

### Advanced Usage

You can combine multiple filters:

```python
proxies = get_proxies(country_code='US', anonymity='elite proxy', https=True, google=True, last_checked_max=600)
```

## License

This project is under the MIT License - see the [LICENSE](LICENSE) file for details.

## Tests

You can run the tests using the `unittest` framework with the command:

```bash
python -m unittest tests/test_proxygetter.py
```