from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import PushEndpoint


class PushClient(BaseQ2Client):

    def get_push_notification_targets(self):
        endpoint = PushEndpoint.PUSH.value
        return self._get(url=self._build_url(endpoint))

    def create_push_notification_target(self, **request_body):
        endpoint = PushEndpoint.PUSH.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_push_notification_target(self, q2_token):
        endpoint = PushEndpoint.PUSH_TOKEN.value.format(qtwoToken=q2_token)
        return self._delete(url=self._build_url(endpoint))

    def update_push_notification_target(self, q2_token, **request_body):
        endpoint = PushEndpoint.PUSH_TOKEN.value.format(qtwoToken=q2_token)
        return self._put(url=self._build_url(endpoint), json=request_body)
