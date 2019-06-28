import json

from   bcm.api.base import BaseAPI

_BIOMODELS_BASE_API_URL = "https://www.ebi.ac.uk/biomodels"

class BioModelsAPI(BaseAPI):
    def __init__(self, accept_format = "json", *args, **kwargs):
        self.accept_format = accept_format

        self.super         = super(BioModelsAPI, self)
        self.super.__init__(base_url = _BIOMODELS_BASE_API_URL, *args, **kwargs)

    def _json_request(self, *args, **kwargs):
        headers = kwargs.pop("headers", { })
        headers.update({
            "Accept": "application/json"
        })

        response = self.super.request(headers = headers, *args, **kwargs)

        text     = response.text
        data     = json.loads(text)

        return data

    def search(self, query, since = 0, size = 100):
        url      = self.build_url("search")

        params   = dict(
            query      = query,
            offset     = since,
            numResults = size
        )

        data     = self._json_request("GET", url, params = params)

        return data

    def model(self, id_):
        url      = self.build_url(id_)
        data     = self._json_request("GET", url)

        return data

    def model_download(self, id_, filename, chunk_yield_size = 1024):
        url      = self.build_url("model", "download", id_)

        params   = dict(
            filename = filename
        )

        response = self.request("GET", url, params = params, stream = True)

        if response.ok:
            for chunk in response.iter_content(chunk_size = chunk_yield_size):
                if chunk:
                    yield chunk
        else:
            response.raise_for_status()

api = BioModelsAPI()