from functools import partial


class HttpApi(object):
    def __init__(self, requests_client, base_url):
        self.http = requests_client
        self.base_url = base_url

    def __call__(self, *args, **kwargs):
        if len(args) == 0:
            return self
        else:
            new_url = self.base_url + "/" + "/".join(args)
            return self.__class__(self.http, new_url)

    def __getattr__(self, key):
        if key in ["put", "get", "post", "delete"]:
            requests_verb = getattr(self.http, key)
            return partial(requests_verb, self.base_url)
        else:
            new_url = self.base_url + "/" + key
            return self.__class__(self.http, new_url)
