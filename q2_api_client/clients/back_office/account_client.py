from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import AccountEndpoint


class AccountClient(BaseQ2Client):

    def retrieve_account(self, account_id):
        """POST /backoffice/v3/account/{id}/retrieve

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.RETRIEVE_ACCOUNT.value.format(id=account_id)
        return self._post(url=self._build_url(endpoint))
