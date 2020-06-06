import setuptools

# include additional packages as well - requests , tabulate , json

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nativeOpenWeather", # Replace with your own username
    version="0.2",
    author="Harsh Native",
    author_email="Harshnative@gmail.com",
    description="Get the weather of any city instantly in your project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/harshnative/nativeOpenWeather_Module",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)