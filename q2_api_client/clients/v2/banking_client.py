from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v2_endpoints import BankingEndpoint


class BankingClient(BaseQ2Client):

    def update_banking_account_status(self, account_id, request_body):
        """PUT /v2/banking/accounts/{id}/statusShortName

        :param str account_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BankingEndpoint.ACCOUNT_STATUS_SHORT_NAME.value.format(id=account_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_banking_groups(self):
        """GET /v2/banking/groups

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BankingEndpoint.GROUPS.value
        return self._get(url=self._build_url(endpoint))

    def create_banking_group(self, request_body):
        """POST /v2/banking/groups

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BankingEndpoint.GROUPS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_banking_groups(self, request_body):
        """PUT /v2/banking/groups

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BankingEndpoint.GROUPS.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_banking_group(self, group_id):
        """DELETE /v2/banking/groups/{group_id}

        :param int group_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BankingEndpoint.GROUP_ID.value.format(group_id=group_id)
        return self._delete(url=self._build_url(endpoint))

    def update_banking_group(self, group_id, request_body):
        """PUT /v2/banking/groups/{group_id}

        :param int group_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BankingEndpoint.GROUP_ID.value.format(group_id=group_id)
        return self._put(url=self._build_url(endpoint), json=request_body)
