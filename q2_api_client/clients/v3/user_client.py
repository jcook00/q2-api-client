from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import UserEndpoint


class UserClient(BaseQ2Client):

    def retrieve_users(self, request_body):
        """POST /v3/user/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_USERS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_self(self):
        """POST /v3/user/retrieveSelf

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_SELF.value
        return self._post(url=self._build_url(endpoint))

    def update_self(self, request_body):
        """POST /v3/user/updateSelf

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.UPDATE_SELF.value
        return self._post(url=self._build_url(endpoint), json=request_body)
