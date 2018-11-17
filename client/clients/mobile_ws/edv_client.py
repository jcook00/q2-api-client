from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import EDVEndpoint


class EDVClient(BaseQ2Client):

    def get_edv(self):
        endpoint = EDVEndpoint.EDV.value
        return self._get(url=self._build_url(endpoint))

    def process_edv(self, **request_body):
        endpoint = EDVEndpoint.EDV.value
        return self._post(url=self._build_url(endpoint), json=request_body)
