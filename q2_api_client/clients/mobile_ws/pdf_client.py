from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import PDFEndpoint


class PDFClient(BaseQ2Client):

    def get_pdf_acceptance_code(self):
        """GET /mobilews/pdf

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PDFEndpoint.PDF.value
        return self._get(url=self._build_url(endpoint))

    def verify_pdf_acceptance_code(self, request_body):
        """PUT /mobilews/pdf/validate

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PDFEndpoint.PDF_VALIDATE.value
        return self._put(url=self._build_url(endpoint), json=request_body)
