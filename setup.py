from setuptools import setup, find_packages

setup(
    name="nelsius-pay",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    author="Nelson Siebi",
    author_email="nelsonsiebi237@gmail.com",
    description="Official Python SDK for Nelsius Pay API V2",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nelson-siebi/nelsius-pay-python",
    license="MIT",
)
