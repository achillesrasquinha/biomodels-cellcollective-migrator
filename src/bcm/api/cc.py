from bcm._compat     import iteritems

import json
from random import randint

from bcm.api.base    import BaseAPI
from bcm.util.system import popen

_CC_BASE_URL = "https://cellcollective.org"

def _import_models_to_save_models(data, user_id):
    models = dict()

    model  = data["1"]

    model                 = dict((k, v) for k, v in iteritems(model) if v)
    model["userId"]       = user_id
    model["type"]         = "research"
    model["components"]   = len([k for k, v in iteritems(model["speciesMap"])])
    model["interactions"] = len([k for k, v in iteritems(model["regulatorMap"])])

    id_ = randint(1000, 9999)

    model["modelVersionMap"] = dict({
        "-%s" % (id_ - 2): dict({
            "name": "1.0"
        })
    })

    models["-%s/-%s" % (id_, id_ - 2)] = model

    return models

class CCAuthenticationError(Exception):
    pass

class CCAPI(BaseAPI):
    def __init__(self, email, password, *args, **kwargs):
        self._email    = email
        self._password = password

        self.super     = super(CCAPI, self)
        self.super.__init__(base_url = _CC_BASE_URL, *args, **kwargs)

        self._login(email, password)

    def _login(self, email, password):
        url       = self.build_url("_api", "login")

        data      = dict(
            username = email,
            password = password
        )
        response  = self.request("POST", url, data = data)

        token     = response.headers.get("x-auth-token")
        
        if not token:
            raise CCAuthenticationError("Unable to authenticate to Cell Collective")
        else:
            self.token = token

        self._get_user_profile()

    def _auth_request(self, *args, **kwargs):
        headers   = kwargs.pop("headers", { })
        headers.update({
            "x-auth-token": self.token
        })

        response  = self.request(headers = headers, *args, **kwargs)

        return response

    def _get_user_profile(self):
        url       = self.build_url("_api", "user", "getProfile")

        response  = self._auth_request("GET", url)

        data      = json.loads(response.text)

        self.user = data

    def import_model(self, filename, save = False):
        url       = self.build_url("_api", "model", "import")
        
        files     = dict({
            "upload": (filename, open(filename, "rb"))
        })

        response  = self._auth_request("POST", url, files = files)

        if save:
            data   = response.content
            data   = json.loads(data)

            models = _import_models_to_save_models(data, user_id = self.user["id"])

            self.save_model(models)

    def save_model(self, model):
        url       = self.build_url("_api", "model", "save")
        headers   = dict({ "Content-Type": "application/json" })
        data      = json.dumps(model)

        response  = self._auth_request("POST", url,
            data    = data,
            headers = headers
        )

        if response.ok:
            return True
        else:
            response.raise_for_status()