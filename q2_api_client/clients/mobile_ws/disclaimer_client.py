from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import DisclaimerEndpoint


class DisclaimerClient(BaseQ2Client):

    def accept_disclaimer(self, request_body):
        """POST /mobilews/disclaimer

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = DisclaimerEndpoint.DISCLAIMER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_disclaimer(self, disclaimer_id):
        """POST /mobilews/disclaimer/{id}

        :param str disclaimer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = DisclaimerEndpoint.DISCLAIMER_ID.value.format(id=disclaimer_id)
        return self._post(url=self._build_url(endpoint))
