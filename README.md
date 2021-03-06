# OmicsDi Fetcher  ![Travis](https://travis-ci.org/bedroesb/omicsdi-cli.svg?branch=master)

Command Line Interface to fetch data from OmicsDI



```
     ___        _       ___  _    __     _      _
    / _ \ _ __ (_)__ __|   \(_)  / _|___| |_ __| |_  ___ _ _
   | (_) | '  \| / _(_-< |) | | |  _/ -_)  _/ _| ' \/ -_) '_|
    \___/|_|_|_|_\__/__/___/|_| |_| \___|\__\__|_||_\___|_|
```

## About
OmicsDi fetcher makes use of the OmicsDi API to find the data file links that belong to a data set accession number.
By default it gives these data links back. Using the `-d` flag it is possible to download the files itself in the working directory or in a specified output directory using the `-o` option. Files are placed in a folder with the accession number as name.

## Installation

Simply use following command line to install OmicsDi fetcher on linux/macOS:

```
sudo python3 -m pip install git+git://github.com/bedroesb/omicsdi-cli.git
```

or this command for Windows (be sure that Python is installed):

```
pip install git+git://github.com/bedroesb/omicsdi-cli.git
```

## Usage

When OmicsDI fetcher is installed correctly it should be available through the command `omicsdi_fetcher`. You can easily test which version is installed with `omicsdi_fetcher -v`. The tool has one mandatory parameter 'accession number' and several options:

```
omicsdi_fetcher [OPTIONS] ACC_NUMBER
```

| Option           | Type | Description                                                                                  |
|------------------|------|----------------------------------------------------------------------------------------------|
|   -v, --version  | FLAG | Print version number                                                                         |
|   -d, --download | FLAG | Use this flag to download the files in the current directory or a specified output directory |
|   -o, --output   | PATH | Output directory when downloading files (default: CWD)                                       |
|   -h, --help     | FLAG | Show this message and exit.                                                                  |

## Examples

- A microarray dataset with ftp links:
    ```
    omicsdi_fetcher E-MTAB-5612
    ```
- Downloading the microarray dataset with ftp links:
    ```
    omicsdi_fetcher E-MTAB-5612 -d
    ```
- A BioModels dataset with https links:
    ```
    omicsdi_fetcher BIOMD0000000048
    ```
- Downloading a dataset in a different directory than CWD:
    ```
    omicsdi_fetcher BIOMD0000000048 -d -o <path to directory>
    ```