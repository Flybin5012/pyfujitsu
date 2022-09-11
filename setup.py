fujitsuimport setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfujitsu",
    version="1.0.0",
    author="Mehdi Modarressi",
    author_email="Luckposht@gmail.com",
    description="Fujitsu Airconditioners",
    long_description="Python library to control Fujitsu General Airconditioners on AylaNetworks IoT platform",
    url="https://github.com/Flybin5012/pyfujitsu",
    packages=setuptools.find_packages(),
    install_requires=['requests','certifi','chardet','idna','urllib3'] ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
