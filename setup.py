import pathlib
from setuptools import setuptools, find_packages, setup, Command

# The directory containing this File
HERE = pathlib.Path(__file__).parent

# The test of the README file
README = (HERE /"README.md").read_text()

#This call to setup() does all the work
setup(
    name="GatorMiner",
    version="1.0.0",
    description="An automatic text mining tool",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Allegheny-Ethical-CS/GatorMiner",
    author="Enpu You",
    author_email="youe2@allegheny.edu",
    packages=find_packages(exclude=("tests",)),
    install_requires=["Git", "Pipenv", "en_core_web_sm", "en_core_web_md"],
)
