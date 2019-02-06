from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import MessageEndpoint


class MessageClient(BaseQ2Client):

    def create_message(self, request_body):
        """POST /v3/message/create

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.CREATE_MESSAGE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_messages(self, request_body):
        """POST /v3/message/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.RETRIEVE_MESSAGES.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_message(self, message_id):
        """POST /v3/account/{id}/retrieve

        :param str message_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.RETRIEVE_MESSAGE.value.format(id=message_id)
        return self._post(url=self._build_url(endpoint))

    def retrieve_unread_message_count(self):
        """POST /v3/message/retrieveUnreadCount

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.RETRIEVE_UNREAD_MESSAGE_COUNT.value
        return self._post(url=self._build_url(endpoint))

    def update_message(self, message_id, request_body):
        """POST /v3/message/{id}/update

        :param str message_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.UPDATE_MESSAGE.value.format(id=message_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
