from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import MessageRecipientGroupEndpoint


class MessageRecipientGroupClient(BaseQ2Client):

    def retrieve_message_recipient_group(self, request_body):
        """POST /v3/messageRecipientGroup/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageRecipientGroupEndpoint.RETRIEVE_MESSAGE_RECIPIENT_GROUP.value
        return self._post(url=self._build_url(endpoint), json=request_body)
