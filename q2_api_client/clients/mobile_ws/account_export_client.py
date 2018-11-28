from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import AccountExportEndpoint


class AccountExportClient(BaseQ2Client):

    def export_account_history(self, account_id, export_format):
        """GET /mobilews/accountExport/{id}/{exportFormat}

        :param str account_id: path parameter
        :param str export_format: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountExportEndpoint.ACCOUNT_EXPORT_FORMAT.value.format(id=account_id, exportFormat=export_format)
        return self._get(url=self._build_url(endpoint))
