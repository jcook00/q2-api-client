from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import RegisterDeviceEndpoint


class RegisterDeviceClient(BaseQ2Client):

    def register_device(self):
        """GET /mobilews/registerDevice

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RegisterDeviceEndpoint.REGISTER_DEVICE.value
        return self._get(url=self._build_url(endpoint))

    def register_notification_room(self, request_body):
        """POST /mobilews/registerNotificationRoom

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RegisterDeviceEndpoint.REGISTER_NOTIFICATION.value
        return self._post(url=self._build_url(endpoint), json=request_body)
