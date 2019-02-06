from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import TACEndpoint


class TACClient(BaseQ2Client):

    def retrieve_tac(self, device_key, request_body):
        """POST /v3/tac/retrieve

        :param str device_key: header
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TACEndpoint.RETRIEVE_TAC.value
        headers = self._copy_headers()
        headers['deviceKey'] = device_key
        return self._post(url=self._build_url(endpoint), headers=headers, json=request_body)

    def generate_tac(self, tac_id, device_key):
        """POST /v3/tac/{id}/generate

        :param str tac_id: path parameter
        :param str device_key: header
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TACEndpoint.GENERATE_TAC.value.format(id=tac_id)
        headers = self._copy_headers()
        headers['deviceKey'] = device_key
        return self._post(url=self._build_url(endpoint), headers=headers)
