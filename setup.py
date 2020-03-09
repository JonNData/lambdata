# setup.py
# instructions for packages...

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="mylambdata",
    version="1.0",
    author="MJ Rossetti",
    author_email="datacreativellc@gmail.com",
    description="for example purposes",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/JonNData/lambdata",
    # keywords="",
    packages=find_packages() 
    # ["my_lambdata"]
)