from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import RegisterDeviceEndpoint


class RegisterDeviceClient(BaseQ2Client):

    def register_device(self):
        endpoint = RegisterDeviceEndpoint.REGISTER_DEVICE.value
        return self._get(url=self._build_url(endpoint))

    def register_notification_room(self, **request_body):
        endpoint = RegisterDeviceEndpoint.REGISTER_NOTIFICATION.value
        return self._post(url=self._build_url(endpoint), json=request_body)
