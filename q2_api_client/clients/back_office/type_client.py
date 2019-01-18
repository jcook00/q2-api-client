from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import TypeEndpoint


class TypeClient(BaseQ2Client):

    def get_action_type(self):
        """GET /backoffice/v3/actionType

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TypeEndpoint.ACTION_TYPE.value
        return self._get(url=self._build_url(endpoint))

    def get_phone_type(self):
        """GET /backoffice/v3/phoneType

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TypeEndpoint.PHONE_TYPE.value
        return self._get(url=self._build_url(endpoint))
