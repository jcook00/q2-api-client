from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import FSFEndpoint


class FSFClient(BaseQ2Client):

    def process_ach_file_stream(self):
        endpoint = FSFEndpoint.FSF.value
        return self._post(url=self._build_url(endpoint))

    def process_message_attachment_file_stream(self):
        endpoint = FSFEndpoint.FSF_ATTACHMENT.value
        return self._post(url=self._build_url(endpoint))
