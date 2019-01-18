from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import ElementEndpoint


class ElementClient(BaseQ2Client):

    def retrieve_elements(self, request_body):
        """POST /v3/element/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ElementEndpoint.RETRIEVE_ELEMENTS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_element(self, element_id):
        """POST /v3/element/{id}/retrieve

        :param str element_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ElementEndpoint.RETRIEVE_ELEMENTS.value.format(id=element_id)
        return self._post(url=self._build_url(endpoint))
