from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import MarketingMessageEndpoint


class MarketingMessageClient(BaseQ2Client):

    def get_marketing_message(self, page_name):
        """GET /mobilews/marketingMessage/{pageNameAndSize}

        :param str page_name: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MarketingMessageEndpoint.MARKETING_MESSAGE.value.format(pageNameAndSize=page_name)
        return self._get(url=self._build_url(endpoint))

    def create_marketing_message_unauth(self, request_body):
        """POST /mobilews/marketingMessageUnauth

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MarketingMessageEndpoint.MARKETING_MESSAGE_UNAUTH.value
        return self._post(url=self._build_url(endpoint), json=request_body)
