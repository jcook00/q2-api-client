from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import PFMAccountEndpoint


class PFMAccountClient(BaseQ2Client):

    def get_pfm_account_permission(self):
        """GET /v3/pfmAccount/permission

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMAccountEndpoint.PFM_ACCOUNT_PERMISSION.value
        return self._get(url=self._build_url(endpoint))

    def retrieve_pfm_accounts(self, request_body):
        """POST /v3/pfmAccount/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMAccountEndpoint.RETRIEVE_PFM_ACCOUNTS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_pfm_account(self, pfm_account_id, request_body):
        """POST /v3/pfmAccount/{id}/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :param str pfm_account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMAccountEndpoint.RETRIEVE_PFM_ACCOUNT.value.format(id=pfm_account_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
