from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import EDVEndpoint


class EDVClient(BaseQ2Client):

    def get_edv(self):
        """GET /mobilews/edv

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = EDVEndpoint.EDV.value
        return self._get(url=self._build_url(endpoint))

    def process_edv(self, request_body):
        """POST /mobilews/edv

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = EDVEndpoint.EDV.value
        return self._post(url=self._build_url(endpoint), json=request_body)
