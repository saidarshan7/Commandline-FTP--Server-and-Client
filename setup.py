from setuptools import setup
from setuptools import find_packages

setup(
    name="ftpclit",
    description="commandline tool to share files in terminal",
    long_description="",
    version="1.1.1",
    url="https://github.com/saidarshan7/Commandline-FTP--Server-and-Client.git",
    author="saidarshan dhadde",
    author_email="saidarshan1430@gmail.com",
    scripts=["scripts/ftpcmd"],
    packages=find_packages("src"),
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python:: 3",
        "License :: OSI Approved ::MIT License",
    ]

)