from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="find-json",
    packages=find_packages(),
    version="0.0.1",
    description="Find keys and variables in a json file",
    long_description=long_description,
    author="Niels Lemmens",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Topic :: Utilities",
    ],
    entry_points={"console_scripts": ["find-json = find_json:main"]},
)
