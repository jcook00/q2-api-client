from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import PasswordEndpoint


class PasswordClient(BaseQ2Client):

    def get_password_permission(self):
        """GET /v3/password/permission

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PasswordEndpoint.PASSWORD_PERMISSION.value
        return self._get(url=self._build_url(endpoint))

    def update_password(self, request_body):
        """POST /v3/password/update

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PasswordEndpoint.UPDATE_PASSWORD.value
        return self._post(url=self._build_url(endpoint), json=request_body)
