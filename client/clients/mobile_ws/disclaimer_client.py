from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import DisclaimerEndpoint


class DisclaimerClient(BaseQ2Client):

    def accept_disclaimer(self, **request_body):
        endpoint = DisclaimerEndpoint.DISCLAIMER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_disclaimer(self, disclaimer_id):
        endpoint = DisclaimerEndpoint.DISCLAIMER_ID.value.format(id=disclaimer_id)
        return self._post(url=self._build_url(endpoint))
