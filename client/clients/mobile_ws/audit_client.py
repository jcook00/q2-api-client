from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AuditEndpoint


class AuditClient(BaseQ2Client):

    def get_audit(self):
        endpoint = AuditEndpoint.AUDIT.value
        return self._get(url=self._build_url(endpoint))

    def create_audit(self, **request_body):
        endpoint = AuditEndpoint.AUDIT.value
        return self._post(url=self._build_url(endpoint), json=request_body)
