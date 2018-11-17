from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AccountsEndpoint


class AccountsClient(BaseQ2Client):

    def get_accounts(self):
        endpoint = AccountsEndpoint.ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))

    def block_accounts(self):
        endpoint = AccountsEndpoint.BLOCK_ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))

    def delete_accounts(self):
        endpoint = AccountsEndpoint.DELETE_ACCOUNTS.value
        return self._get(url=self._build_url(endpoint))
