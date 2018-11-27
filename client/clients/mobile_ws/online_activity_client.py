from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import OnlineActivityEndpoint


class OnlineActivityClient(BaseQ2Client):

    def get_online_activity_export(self, account_id):
        """GET /mobilews/onlineActivityExport/{id}

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = OnlineActivityEndpoint.ONLINE_ACTIVITY_EXPORT.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))
