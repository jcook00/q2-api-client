from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import PushEndpoint


class PushClient(BaseQ2Client):

    def get_push_notification_targets(self):
        """GET /mobilews/push

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PushEndpoint.PUSH.value
        return self._get(url=self._build_url(endpoint))

    def create_push_notification_target(self, request_body):
        """PUSH /mobilews/push

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PushEndpoint.PUSH.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_push_notification_target(self, q2_token):
        """DELETE /mobilews/push/{qtwoToken}

        :param str q2_token: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PushEndpoint.PUSH_TOKEN.value.format(qtwoToken=q2_token)
        return self._delete(url=self._build_url(endpoint))

    def update_push_notification_target(self, q2_token, request_body):
        """PUT /mobilews/push/{qtwoToken}

        :param str q2_token: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PushEndpoint.PUSH_TOKEN.value.format(qtwoToken=q2_token)
        return self._put(url=self._build_url(endpoint), json=request_body)
