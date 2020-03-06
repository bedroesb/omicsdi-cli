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

@click.command()
@click.argument('acc')
def main(acc):
    source = source_from_id(acc)
    ftp = ftp_links(source, acc)
    output = '\n'.join(ftp)
    print(output)


if __name__ == "__main__":
    main()
