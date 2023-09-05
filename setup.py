from setuptools import setup, find_packages

setup(
    name="proxygetter",
    version="0.1.0",
    url="https://github.com/ArthurVerrez/proxygetter",
    author="Arthur Verrez",
    author_email="macdouglass@example.com",
    description="A utility to get and filter proxies",
    packages=find_packages(),
    install_requires=["requests", "beautifulsoup4"],
)
