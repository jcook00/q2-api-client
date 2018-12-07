from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import OnlineActivityEndpoint


class OnlineActivityClient(BaseQ2Client):

    def get_online_activity_export(self, activity_id, **query):
        """GET /mobilews/onlineActivityExport/{id}

        :param str activity_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = OnlineActivityEndpoint.ONLINE_ACTIVITY_EXPORT.value.format(id=activity_id)
        query_parameters = self._copy_query_parameters()
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)
