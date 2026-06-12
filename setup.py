from setuptools import setup, find_packages

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()

setup(
    name="MLOPS-PROJECT-1",
    version="0.1",
    author="shantanu",
    packages=find_packages(),
    install_requires=requirements,
)