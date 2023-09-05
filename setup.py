from setuptools import setup, find_packages


def read_requirements():
    with open("requirements.txt", "r") as req_file:
        return [line.strip() for line in req_file.readlines()]


# Read the contents of your README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="proxygetter",
    version="0.1.0",
    url="https://github.com/ArthurVerrez/proxygetter",
    author="Arthur Verrez",
    author_email="macdouglass@outlook.com",
    description="A utility to get and filter free proxies",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=read_requirements(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
