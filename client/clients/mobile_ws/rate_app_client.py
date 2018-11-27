from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import RateAppEndpoint


class RateAppClient(BaseQ2Client):

    def decline_rate_app(self):
        """PUT /mobilews/rateApp/decline

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RateAppEndpoint.RATE_DECLINE.value
        return self._put(url=self._build_url(endpoint))

    def rate_app(self):
        """PUT /mobilews/rateApp/rate

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RateAppEndpoint.RATE.value
        return self._put(url=self._build_url(endpoint))
