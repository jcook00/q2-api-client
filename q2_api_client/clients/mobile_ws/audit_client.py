from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import AuditEndpoint


class AuditClient(BaseQ2Client):

    def get_audit(self):
        """GET /mobilews/audit

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuditEndpoint.AUDIT.value
        return self._get(url=self._build_url(endpoint))

    def create_audit(self, request_body):
        """POST /mobilews/audit

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuditEndpoint.AUDIT.value
        return self._post(url=self._build_url(endpoint), json=request_body)
