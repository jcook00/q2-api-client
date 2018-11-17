from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import MessageEndpoint


class MessageClient(BaseQ2Client):

    def get_messages(self):
        endpoint = MessageEndpoint.MESSAGE.value
        return self._get(url=self._build_url(endpoint))

    def send_message(self, **request_body):
        endpoint = MessageEndpoint.MESSAGE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def mark_message_as_read(self, **request_body):
        endpoint = MessageEndpoint.MESSAGE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_message_attachments(self):
        endpoint = MessageEndpoint.MESSAGE_ATTACHMENT.value
        return self._get(url=self._build_url(endpoint))

    def get_message_attachment(self, attachment_id):
        endpoint = MessageEndpoint.MESSAGE_ATTACHMENT_ID.value.format(id=attachment_id)
        return self._get(url=self._build_url(endpoint))

    def get_message_count(self):
        endpoint = MessageEndpoint.MESSAGE_COUNT.value
        return self._get(url=self._build_url(endpoint))

    def delete_messages(self, **request_body):
        endpoint = MessageEndpoint.MESSAGE_DELETE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def remove_message_expiration(self, **request_body):
        endpoint = MessageEndpoint.MESSAGE_EXPIRE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_message_recipients(self):
        endpoint = MessageEndpoint.MESSAGE_RECIPIENT.value
        return self._get(url=self._build_url(endpoint))

    def get_message(self, message_id):
        endpoint = MessageEndpoint.MESSAGE_ID.value.format(id=message_id)
        return self._get(url=self._build_url(endpoint))

    def delete_message(self, message_id):
        endpoint = MessageEndpoint.MESSAGE_ID.value.format(id=message_id)
        return self._delete(url=self._build_url(endpoint))

    def send_reply_message(self, message_id, **request_body):
        endpoint = MessageEndpoint.MESSAGE_ID.value.format(id=message_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
