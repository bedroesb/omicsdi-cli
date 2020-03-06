import click
from omics_client import OmcicsClient
import os

client = OmcicsClient()


def source_from_id(acc):
    api_output = client.get_source(acc)
    source = api_output['datasets'][0]['source']
    return source


def ftp_links(source, acc):
    api_output = client.get_data(source, acc)
    ftp = []
    files = api_output['file_versions'][0]['files']

    for ext, file_links in files.items():
        for file_link in file_links:
            ftp.append(file_link)
    return ftp


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.argument('acc_number')
@click.option(
    '--download', '-d',  is_flag=True,
    help='Use this flag to download the files in the current directory',
)
@click.option(
    '--output', '-o',  default='/',  type=click.Path(exists=True),
    help='Output file (default: stdout)',
)
def main(acc_number, download, output):
    """
\b
   ___        _       ___  _     ___ _    ___ 
  / _ \ _ __ (_)__ __|   \(_)   / __| |  |_ _|
 | (_) | '  \| / _(_-< |) | |  | (__| |__ | | 
  \___/|_|_|_|_\__/__/___/|_|   \___|____|___|                                           
\b                                                   
    A little OmicsDi data fetcher tool.
    """

    source = source_from_id(acc_number)
    ftps = ftp_links(source, acc_number)

    if download:
        client.download_files(ftps[0], output, acc_number)
    else:
        pretty = '\n'.join(ftps)
        print(pretty)


if __name__ == "__main__":
    main()
