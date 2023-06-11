import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="Text-Summarizer",
    version="0.0.0",
    author="SUMITDHAKAD0",
    author_email="sumit.dhakad9644@gmail.com",
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/SUMITDHAKAD0/Text-Summarizer",
    project_urls={
        "Bug Tracker": f"https://github.com/SUMITDHAKAD0/Text-Summarizer/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)