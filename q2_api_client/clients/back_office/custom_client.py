from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import CustomEndpoint


class CustomClient(BaseQ2Client):

    def search_deleted(self, request_body):
        """POST /custom/associate/searchDeleted

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CustomEndpoint.SEARCH_DELETED.value
        return self._post(url=self._build_url(endpoint), json=request_body)
