from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='OmicsDi_fetcher',
    version='0.1',
    description='A little OmicsDi data fetcher tool',
    long_description=long_description,
    author='Bert Droesbeke',
    author_email='bedro@psb.ugent.be',
    packages=['.'],
    install_requires=['click'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.5',
    entry_points={
        "console_scripts": [
            "omicsdi_fetcher = omicsdi_fetcher:main"
        ]
    },
)
