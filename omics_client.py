import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import ftplib
import time
import re
import shutil
from urllib.parse import urlsplit
import os


def url_path_join(*args):
    """Join path(s) in URL using slashes"""

    return '/'.join(s.strip('/') for s in args)

def url_process(url):
    if not '://' in url:
        if url.startswith('ftp.'):
            newurl = 'ftp://' + url
            return newurl
        else:
            newurl = 'https://' + url
            return newurl
    else:
        return url

class OmcicsClient:
    def __init__(self):
        self.endpoint = 'https://www.omicsdi.org:443/'

    def get_source(self, acc_numb):
        """"Get source from Id"""

        return self.fetch_object(f'/ws/dataset//search?query={acc_numb}')

    def get_data(self, source, acc_numb):
        """"Get ftp links from Id"""

        return self.fetch_object(f'/ws/dataset/{source}/{acc_numb}')

    def fetch_object(self, path):
        """API object fetcher"""

        url = url_path_join(self.endpoint, path)
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=15)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        r = session.get(url)
        # Covering internal server errors by retrying one more time
        if r.status_code == 500:
            time.sleep(5)
            r = requests.get(url)
        elif r.status_code != requests.codes.ok:
            print("problem with request: " + str(r))
            raise RuntimeError("Non-200 status code")
        return r.json()

    def download_files(self, url, output, acc_number):
        """Download files in given directory"""

        split_url = urlsplit(url_process(url))
        project_dir = "".join(split_url.path.rpartition("/")[:-1])
        domain = split_url.hostname
        scheme = split_url.scheme

        
        if scheme == 'ftp':
            with ftplib.FTP(domain) as ftp:
                try:
                    ftp.login()
                    ftp.cwd(project_dir)
                    if output:
                        dir_path = url_path_join(output, acc_number)
                    else:
                        dir_path = acc_number

                    if os.path.exists(dir_path):
                        shutil.rmtree(dir_path)
                    os.makedirs(dir_path)
                    files = ftp.nlst()
                    
                    for ftp_file in files:
                        print("Downloading...  " + ftp_file)
                        file_path = url_path_join(dir_path, ftp_file)
                        localfile = open(file_path, 'wb')
                        ftp.retrbinary(
                            "RETR " + ftp_file, localfile.write)
                        localfile.close()


                except ftplib.all_errors as e:
                    print('FTP error:', e)
        
        elif scheme == 'https' or scheme == 'http':
            

        else:
            print('Scheme is not supported.')

