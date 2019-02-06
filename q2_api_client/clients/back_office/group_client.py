from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import GroupEndpoint


class GroupClient(BaseQ2Client):

    def retrieve_group(self, group_id):
        """POST /backoffice/v3/group/{id}/retrieve

        :param str group_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GroupEndpoint.RETRIEVE_GROUP.value.format(id=group_id)
        return self._post(url=self._build_url(endpoint))
