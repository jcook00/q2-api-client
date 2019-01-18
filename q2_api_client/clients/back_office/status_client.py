from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import StatusEndpoint


class StatusClient(BaseQ2Client):

    def get_user_login_statuses(self):
        """GET /backoffice/v3/userLoginStatus

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = StatusEndpoint.USER_LOGIN_STATUS.value
        return self._get(url=self._build_url(endpoint))

    def get_user_statuses(self):
        """GET /backoffice/v3/userStatus

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = StatusEndpoint.USER_STATUS.value
        return self._get(url=self._build_url(endpoint))
