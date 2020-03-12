# OmicsDi Fetcher  ![Travis](https://travis-ci.org/bedroesb/omicsdi-cli.svg?branch=master)

Command Line Interface to fetch data from OmicsDI



```
     ___        _       ___  _    __     _      _
    / _ \ _ __ (_)__ __|   \(_)  / _|___| |_ __| |_  ___ _ _
   | (_) | '  \| / _(_-< |) | | |  _/ -_)  _/ _| ' \/ -_) '_|
    \___/|_|_|_|_\__/__/___/|_| |_| \___|\__\__|_||_\___|_|

```

## Installation

```
pip install git+git://github.com/bedroesb/omicsdi-cli.git
```

## Usage

```
omicsdi_fetcher [OPTIONS] ACC_NUMBER
```

| Option           | Type | Description                                                                                  |
|------------------|------|----------------------------------------------------------------------------------------------|
|   -v, --version  | FLAG | Print version number                                                                         |
|   -d, --download | FLAG | Use this flag to download the files in the current directory or a specified output directory |
|   -o, --output   | PATH | Output directory when downloading files (default: CWD)                                       |
|   -h, --help     | FLAG | Show this message and exit.                                                                  |