# setup.py

from setuptools import setup, find_packages

setup(
    name="disk_usage",  # The name of your package
    version="0.1",  # The initial release version
    packages=find_packages(),  # Automatically find package directories
    description="A Python package to read disk usage",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Shourya Wadhwa",
    author_email="sourceboxtv@gmail.com",
    url="https://github.com/CoderLogy/Python-Disk-Usage",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL version 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
