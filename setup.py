import os.path
import pathlib
import subprocess

import setuptools
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# version
alphavantage_api_client_version = subprocess.run(['git', 'describe', '--tags'],
                                                     stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
assert "." in alphavantage_api_client_version
assert os.path.isfile("alphavantage_api_client/version.py")
#with open("alphavantage_api_client/VERSION","w", encoding="utf-8") as fh:
#    fh.write(f'{alphavantage_api_client_version}\n')

# This call to setup() does all the work
setup(
    name="alphavantage-api-client",
    version=alphavantage_api_client_version,
    description="Interact with Alphavantage REST API",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/xrgarcia/alphavantage-api-client",
    author="Slashbin, LLC",
    author_email="support@slashbin.us",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=setuptools.find_packages(),
    package_data={},
    include_package_data=True,
    install_requires=["requests"],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "alphavantageapiclient=__main__:main",
        ]
    },
)