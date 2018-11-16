from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import LanguageEndpoint


class LanguageClient(BaseQ2Client):

    def get_languages(self):
        endpoint = LanguageEndpoint.LANGUAGE.value
        return self._get(url=self._build_url(endpoint))
