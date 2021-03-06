import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="libsm",
    version="0.1.0",
    author="vang1ong7ang",
    author_email="vang1ong7ang@outlook.com",
    description="An academic library for state machinev specification and model checking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/libsm/libsm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
