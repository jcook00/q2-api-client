from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import MicroDepositEndpoint


class MicroDepositClient(BaseQ2Client):

    def get_micro_deposits(self):
        endpoint = MicroDepositEndpoint.MICRODEPOSIT.value
        return self._get(url=self._build_url(endpoint))

    def create_micro_deposit(self, **request_body):
        endpoint = MicroDepositEndpoint.MICRODEPOSIT.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def verify_micro_deposit(self, deposit_id, **request_body):
        endpoint = MicroDepositEndpoint.MICRODEPOSIT_ID.value.format(id=deposit_id)
        return self._put(url=self._build_url(endpoint), json=request_body)
