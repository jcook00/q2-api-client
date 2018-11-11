from client.clients.q2_client import Q2Client
from client.endpoints.v2 import BankingEndpoint


class BankingClient(Q2Client):

    def update_banking_account_status(self, account_id, **request_body):
        endpoint = BankingEndpoint.ACCOUNT_STATUS_SHORT_NAME.value.format(id=account_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_banking_groups(self):
        endpoint = BankingEndpoint.GROUPS.value
        return self._get(url=self._build_url(endpoint))

    def create_banking_group(self, **request_body):
        endpoint = BankingEndpoint.GROUPS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_banking_groups(self, **request_body):
        endpoint = BankingEndpoint.GROUPS.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_banking_group(self, group_id):
        endpoint = BankingEndpoint.GROUP_ID.value.format(group_id=group_id)
        return self._delete(url=self._build_url(endpoint))

    def update_banking_group(self, group_id, **request_body):
        endpoint = BankingEndpoint.GROUP_ID.value.format(group_id=group_id)
        return self._put(url=self._build_url(endpoint), json=request_body)
