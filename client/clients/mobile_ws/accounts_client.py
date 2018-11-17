from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AccountsEndpoint


class AccountsClient(BaseQ2Client):

    def get_accounts(self):
        """GET /mobilews/accounts

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountsEndpoint.ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))

    def block_accounts(self):
        """GET /mobilews/accounts/block

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountsEndpoint.BLOCK_ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))

    def delete_accounts(self):
        """GET /mobilews/accounts/delete

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountsEndpoint.DELETE_ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))
