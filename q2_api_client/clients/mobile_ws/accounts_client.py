from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import AccountsEndpoint
from q2_api_client.utils.retry import retry


class AccountsClient(BaseQ2Client):

    @retry(raise_for_status=True)
    def get_accounts(self):
        """GET /mobilews/accounts

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountsEndpoint.ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))

    def get_blocked_accounts(self):
        """GET /mobilews/accounts/block

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountsEndpoint.BLOCK_ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))

    def get_deleted_accounts(self):
        """GET /mobilews/accounts/delete

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountsEndpoint.DELETE_ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))
