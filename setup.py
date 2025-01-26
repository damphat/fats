from setuptools import setup, find_packages

__version__ = "0.2"
setup(
    name="fats",
    version="0.2",
    packages=find_packages(),
    # dependencies
    install_requires=[
        "numpy",
        "matplotlib",
    ],
)