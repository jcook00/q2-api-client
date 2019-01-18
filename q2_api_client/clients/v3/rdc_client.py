from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import RDCEndpoint


class RDCClient(BaseQ2Client):

    def get_rdc_permission(self):
        """GET /v3/rdc/permission

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RDC_PERMISSIONS.value
        return self._get(url=self._build_url(endpoint))

    def create_rdc(self, request_body):
        """POST /v3/rdc/create

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.CREATE_RDC.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_rdc_history(self, request_body):
        """POST /v3/rdc/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RETRIEVE_RDCS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_rdc(self, rdc_id):
        """POST /v3/rdc/{id}/retrieve

        :param str rdc_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RETRIEVE_RDC.value.format(id=rdc_id)
        return self._post(url=self._build_url(endpoint))
