#!/usr/bin/env python

from setuptools import setup, find_packages
import sys
from collections import OrderedDict

DESCRIPTION = "Python with RabbitMQ—simplified so you won't have to."
LONG_DESCRIPTION = open("README.md").read()
VERSION = "0.1.0"

setup_requires = (
    ["pytest-runner"] if any(x in sys.argv for x in ("pytest", "test", "ptr")) else []
)


setup(
    name="PyRMQ",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Alexandre Gerona",
    author_email="alecgerona@gmail.com",
    maintainer="Jasper Sibayan",
    maintainer_email="jasper.sibayan@firstdigitalfinance.com",
    url="https://pyrmq.readthedocs.io",
    project_urls=OrderedDict(
        (
            ("Documentation", "https://pyrmq.readthedocs.io"),
            ("Code", "https://github.com/altusgerona/pyrmq"),
            ("Issue tracker", "https://github.com/altusgerona/pyrmq/issues"),
        )
    ),
    license="ISC",
    platforms=["any"],
    packages=find_packages(include="pyrmq"),
    include_package_data=True,
    setup_requires=setup_requires,
    tests_require=["pytest"],
    test_suite="pyrmq.tests",
    install_requires=["setuptools", "pika"],
    keywords=["rabbitmq", "pika", "consumer", "publisher", "queue", "messages"],
    python_requires=">=3.5",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License (MIT)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)
