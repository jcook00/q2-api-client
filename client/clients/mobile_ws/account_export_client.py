from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AccountExportEndpoint


class AccountExportClient(BaseQ2Client):

    def export_account_history(self, account_id, export_format):
        endpoint = AccountExportEndpoint.ACCOUNT_EXPORT_FORMAT.value.format(id=account_id, exportFormat=export_format)
        return self._get(url=self._build_url(endpoint))
