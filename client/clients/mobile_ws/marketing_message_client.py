from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import MarketingMessageEndpoint


class MarketingMessageClient(BaseQ2Client):

    def get_marketing_message(self, page_name):
        endpoint = MarketingMessageEndpoint.MARKETING_MESSAGE.value.format(pageNameAndSize=page_name)
        return self._get(url=self._build_url(endpoint))

    def create_marketing_message_unauth(self, **request_body):
        endpoint = MarketingMessageEndpoint.MARKETING_MESSAGE_UNAUTH.value
        return self._post(url=self._build_url(endpoint), json=request_body)
