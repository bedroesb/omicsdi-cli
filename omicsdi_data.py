import click
from omics_client import OmcicsClient

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
def main(acc_number):
    """
\b
   ____            _          _____ _____    _____ _      _____ 
  / __ \          (_)        |  __ \_   _|  / ____| |    |_   _|
 | |  | |_ __ ___  _  ___ ___| |  | || |   | |    | |      | |  
 | |  | | '_ ` _ \| |/ __/ __| |  | || |   | |    | |      | |  
 | |__| | | | | | | | (__\__ \ |__| || |_  | |____| |____ _| |_ 
  \____/|_| |_| |_|_|\___|___/_____/_____|  \_____|______|_____|
\b                                                   

    A little OmicsDI data fetcher tool.
    """
    source = source_from_id(acc_number)
    ftp = ftp_links(source, acc_number)
    output = '\n'.join(ftp)
    print(output)


if __name__ == "__main__":
    main()
