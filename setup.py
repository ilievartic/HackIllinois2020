import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='goliath',  
    version='0.1.2.1',
    scripts=['goliath'] ,
    author="Ilie Vartic",
    author_email="ilie.vartic@gmail.com",
    description="This package enables Python to offload sets of function calls to pools of remote worker processes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ilievartic/Goliath/archive/v0.1.2.1.tar.gz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
)
