import json

from bcm._compat  import urljoin
from bcm          import request as req

class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def build_url(self, *slug):
        url = "/".join([self.base_url, *slug])
        return url

    def request(self, method, url, raise_err = True, *args, **kwargs):
        headers  = kwargs.pop("headers", { })
        response = req.request(method, url, headers = headers, *args, **kwargs)

        return response