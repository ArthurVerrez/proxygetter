from setuptools import setup, find_packages

setup(
    name="proxygetter",
    version="0.1.0",
    url="https://github.com/ArthurVerrez/proxygetter",
    author="Arthur Verrez",
    author_email="macdouglass@example.com",
    description="A utility to get and filter free proxies",
    packages=find_packages(),
    install_requires=["requests", "beautifulsoup4"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
