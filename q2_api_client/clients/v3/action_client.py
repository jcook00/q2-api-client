from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import ActionEndpoint


class ActionClient(BaseQ2Client):

    def retrieve_actions(self, request_body):
        """POST /v3/action/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ActionEndpoint.RETRIEVE_ACTIONS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_action(self, action_id):
        """POST /v3/action/{id}/retrieve

        :param str action_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ActionEndpoint.RETRIEVE_ACTION.value.format(id=action_id)
        return self._post(url=self._build_url(endpoint))
