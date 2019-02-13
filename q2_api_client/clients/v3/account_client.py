from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import AccountEndpoint


class AccountClient(BaseQ2Client):

    def retrieve_accounts(self, request_body):
        """POST /v3/account/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.RETRIEVE_ACCOUNTS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_account(self, account_id):
        """POST /v3/account/{id}/retrieve

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.RETRIEVE_ACCOUNT.value.format(id=account_id)
        return self._post(url=self._build_url(endpoint))

    def update_account(self, account_id, request_body):
        """POST /v3/account/{id}/update

        :param str account_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.UPDATE_ACCOUNT.value.format(id=account_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
