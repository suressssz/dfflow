from setuptools import setup, find_packages

# Read requirements.txt for install_requires
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="dfflow",
    version="0.1.0",
    author="Suresh K",
    description="Lightweight pandas DataFrame logging and flow tracker",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/suressssz/dfflow",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
