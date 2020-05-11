from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='OmicsDi_fetcher',
    version='0.1',
    keywords=["pip", "omicsDI", "cli"],
    description='Command Line Interface to fetch data from OmicsDi',
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='Bert Droesbeke',
    url="https://github.com/bedroesb/omicsdi-cli",
    author_email='bedro@psb.ugent.be',
    packages=['.'],
    install_requires=[required],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "omicsdi_fetcher = omicsdi_fetcher:main"
        ]
    },
)
