from setuptools import setup, find_packages

setup(
    name="DASST",  # The name of your package
    version="0.0.1",  # The initial release version
    packages=find_packages(),  # Automatically find package directories
    description="A Python package to read system usage also known as Disk And System Stats Tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Shourya Wadhwa",
    author_email="sourceboxtv@gmail.com",
    url="https://github.com/CoderLogy/DASST",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "psutil"
    ],
    include_package_data=True,
    license="GPL-3.0-or-later",
    license_files=('LICENSE'),
)
