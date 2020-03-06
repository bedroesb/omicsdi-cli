import argparse
from sys import argv
from omics_client import OmcicsClient

acc_number = argv[1]
client = OmcicsClient()

def source_from_id(acc):
    api_output = client.get_source(acc)
    source = api_output['datasets'][0]['source']
    return source

def ftp_links(source, acc):
    api_output = client.get_data(source, acc)
    ftp = []
    files = api_output['file_versions'][0]['files']
    
    for ext,file_links in files.items():
        for file_link in file_links:
            ftp.append(file_link)
    return ftp


def ftp_from_id(acc):
    source = source_from_id(acc)
    ftp = ftp_links(source, acc)
    return ftp


print('\n'.join(ftp_from_id(acc_number)))
