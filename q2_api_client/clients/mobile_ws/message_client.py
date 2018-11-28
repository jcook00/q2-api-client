from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import MessageEndpoint


class MessageClient(BaseQ2Client):

    def get_messages(self):
        """GET /mobilews/message

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE.value
        return self._get(url=self._build_url(endpoint))

    def send_message(self, request_body):
        """POST /mobilews/message

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def mark_message_as_read(self, request_body):
        """PUT /mobilews/message

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_message_attachments(self):
        """GET /mobilews/message/attachment

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_ATTACHMENT.value
        return self._get(url=self._build_url(endpoint))

    def get_message_attachment(self, attachment_id):
        """GET /mobilews/message/attachment/{id}

        :param str attachment_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_ATTACHMENT_ID.value.format(id=attachment_id)
        return self._get(url=self._build_url(endpoint))

    def get_message_count(self):
        """GET /mobilews/message/count

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_COUNT.value
        return self._get(url=self._build_url(endpoint))

    def delete_messages(self, request_body):
        """PUT /mobilews/message/delete

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_DELETE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def remove_message_expiration(self, request_body):
        """PUT /mobilews/message/expire

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_EXPIRE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_message_recipients(self):
        """GET /mobilews/message/messageRecipient

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_RECIPIENT.value
        return self._get(url=self._build_url(endpoint))

    def get_message(self, message_id):
        """GET /mobilews/message/{id}

        :param str message_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_ID.value.format(id=message_id)
        return self._get(url=self._build_url(endpoint))

    def delete_message(self, message_id):
        """DELETE /mobilews/message/{id}

        :param str message_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_ID.value.format(id=message_id)
        return self._delete(url=self._build_url(endpoint))

    def send_reply_message(self, message_id, request_body):
        """POST /mobilews/message/{id}

        :param str message_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MessageEndpoint.MESSAGE_ID.value.format(id=message_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
