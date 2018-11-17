from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AccountPFMEndpoint


class AccountPFMClient(BaseQ2Client):

    def get_pfm_accounts(self):
        """GET /mobilews/accountPfm

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountPFMEndpoint.ACCOUNT_PFM.value
        return self._get(url=self._build_url(endpoint))

    def get_pfm_accounts_data(self):
        """GET /mobilews/accountPfm/data

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountPFMEndpoint.ACCOUNT_PFM_DATA.value
        return self._get(url=self._build_url(endpoint))

    def get_pfm_account(self, account_id):
        """GET /mobilews/accountPfm/{id}

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountPFMEndpoint.ACCOUNT_PFM_ID.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_pfm_account_history(self, account_id):
        """GET /mobilews/accountPfm/{id}/history

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountPFMEndpoint.ACCOUNT_PFM_HISTORY.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def export_pfm_account_history(self, account_id, export_format):
        """GET /mobilews/accountPfmExport/{id}/{exportFormat}

        :param str account_id: path parameter
        :param str export_format: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountPFMEndpoint.ACCOUNT_PFM_EXPORT.value.format(id=account_id, exportFormat=export_format)
        return self._get(url=self._build_url(endpoint))
