import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jplotlib",
    version="1.0.1",
    author="Jacob Valdez",
    author_email="jacobfv@msn.com",
    description="Simple plotting utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JacobFV/jplotlib",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)