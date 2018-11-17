from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import MicroDepositEndpoint


class MicroDepositClient(BaseQ2Client):

    def get_micro_deposits(self):
        """GET /mobilews/microdeposit

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MicroDepositEndpoint.MICRO_DEPOSIT.value
        return self._get(url=self._build_url(endpoint))

    def create_micro_deposit(self, request_body):
        """POST /mobilews/microdeposit

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MicroDepositEndpoint.MICRO_DEPOSIT.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def verify_micro_deposit(self, deposit_id, request_body):
        """PUT /mobilews/microdeposit/{id}

        :param str deposit_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = MicroDepositEndpoint.MICRO_DEPOSIT_ID.value.format(id=deposit_id)
        return self._put(url=self._build_url(endpoint), json=request_body)
