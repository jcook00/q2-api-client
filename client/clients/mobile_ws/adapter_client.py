from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AdapterEndpoint


class AdapterClient(BaseQ2Client):

    def adapter_pass_through_vendor_with_account(self, vendor_id, account_id, **request_body):
        endpoint = AdapterEndpoint.ADAPTER.value.format(vendorId=vendor_id, accountId=account_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
