# imports - compatibility imports
from bcm._compat import (
    urlopen,
    Request,
    urlencode,
    HTTPError,
    ModuleNotFoundError
)

# imports - standard imports
import json

# imports - module imports
from bcm.request.response import Response
from bcm.util.string      import safe_encode

# YAGNI: This patched "requests" works only for bcm's use-cases.

def request(method, url, **kwargs):
    try:
        import requests as req
        return req.request(method, url, **kwargs)
    except (ImportError, ModuleNotFoundError):
        method = method.lower()

        if   method == "get":
            return get(url, **kwargs)
        elif method == "post":
            return post(url, **kwargs)
        else:
            raise ValueError("Unknown method %s" % method)

def get(*args, **kwargs):
    try:
        import requests as req
        return req.get(*args, **kwargs)
    except (ImportError, ModuleNotFoundError):
        url      = args[0]
        response = Response()

        try:
            http_response    = urlopen(url)
            status_code      = http_response.getcode()

            response.content = http_response.read()

            http_response.close()
        except HTTPError as e:
            status_code      = e.getcode()

        response.url         = url
        response.status_code = status_code

        return response

def post(*args, **kwargs):
    try:
        import requests as req
        return req.post(*args, **kwargs)
    except (ImportError, ModuleNotFoundError):
        url      = args[0]
        data     = kwargs.get("data",    { })
        headers  = kwargs.get("headers", { })

        response = Response()
        
        try:
            data             = safe_encode(urlencode(data))
            request          = Request(url, data = data, headers = headers)
            http_response    = urlopen(request)

            response.content = http_response.read()

            http_response.close()
        except HTTPError as e:
            status_code      = e.getcode()

        response.url         = url
        response.status_code = status_code

        return response