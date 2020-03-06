import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import ftplib
import time
import re
from urllib.parse import urlsplit
import os


def url_path_join(*args):
    """Join path(s) in URL using slashes"""

    return '/'.join(s.strip('/') for s in args)


class OmcicsClient:
    def __init__(self):
        self.endpoint = 'https://www.omicsdi.org:443/'
        self.ftp = 'ftp.ebi.ac.uk'

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

        split_url = urlsplit(url)
        clean_path = "".join(split_url.path.rpartition("/")[:-1])
        
        with ftplib.FTP(self.ftp) as ftp:
            try:
                ftp.login()
                ftp.cwd(clean_path)
                if output:
                    dir_path = url_path_join(output, acc_number)
                else:
                    dir_path = acc_number
                os.makedirs(dir_path) 
                files = ftp.nlst()
                
                for ftp_file in files:
                    print("Downloading...  " + ftp_file)
                    file_path = url_path_join(output, acc_number, ftp_file)
                    localfile = open(file_path, 'wb')
                    ftp.retrbinary(
                        "RETR " + ftp_file, localfile.write)
                    localfile.close()


            except ftplib.all_errors as e:
                print('FTP error:', e)
