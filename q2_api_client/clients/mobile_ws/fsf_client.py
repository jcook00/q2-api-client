from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import FSFEndpoint


class FSFClient(BaseQ2Client):

    def process_ach_file_stream(self):
        """POST /mobilews/fsf

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FSFEndpoint.FSF.value
        return self._post(url=self._build_url(endpoint))

    def process_message_attachment_file_stream(self):
        """POST /mobilews/fsf/attachment

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FSFEndpoint.FSF_ATTACHMENT.value
        return self._post(url=self._build_url(endpoint))
