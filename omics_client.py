import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
import re


def url_path_join(*args):
    """Join path(s) in URL using slashes"""
    return '/'.join(s.strip('/') for s in args)


class OmcicsClient:
    def __init__(self):
        self.endpoint = 'https://www.omicsdi.org:443/'

    def get_source(self, acc_numb: str) -> dict:
        """"Get source from Id"""
        return self.fetch_object(f'/ws/dataset//search?query={acc_numb}')

    def get_data(self, source, acc_numb: str) -> dict:
        """"Get ftp links from Id"""
        return self.fetch_object(f'/ws/dataset/{source}/{acc_numb}')

    def fetch_object(self, path: str) -> dict:
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
