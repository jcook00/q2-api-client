from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import PDFEndpoint


class PDFClient(BaseQ2Client):

    def get_pdf_acceptance_code(self):
        endpoint = PDFEndpoint.PDF.value
        return self._get(url=self._build_url(endpoint))

    def verify_pdf_acceptance_code(self, **request_body):
        endpoint = PDFEndpoint.PDF_VALIDATE.value
        return self._put(url=self._build_url(endpoint), json=request_body)
