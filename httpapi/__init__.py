from functools import partial
from requests import Session
from urllib import parse as urlparse


session = Session()


class HttpApi(object):
    def __init__(self, base_url, requests_client=session):
        self.http = requests_client
        self.base_url = base_url

    def __call__(self, *args, **kwargs):
        if len(args) == 0:
            return self
        else:
            new_url = urlparse.urljoin(
                self.base_url, "/".join(str(arg) for arg in args)
            )
            return self.__class__(new_url, self.http)

    def __getattr__(self, key):
        if key in ["put", "get", "post", "delete"]:
            requests_verb = getattr(self.http, key)
            return partial(requests_verb, self.base_url)
        else:
            new_url = urlparse.urljoin(self.base_url, "/" + str(key))
            return self.__class__(new_url, self.http)
