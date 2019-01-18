from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import CSRAssistEndpoint


class CSRAssistClient(BaseQ2Client):

    def create_csr_assist(self, request_body):
        """POST /backoffice/v3/csrAssist/create

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSRAssistEndpoint.CREATE_CSR_ASSIST.value
        return self._post(url=self._build_url(endpoint), json=request_body)
