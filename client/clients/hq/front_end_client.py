from client.clients.q2_client import Q2Client
from client.endpoints.hq import FrontEndEndpoint


class FrontEndClient(Q2Client):

    def get_dispute_form(self):
        endpoint = FrontEndEndpoint.DISPUTE_FORM.value
        return self.get(url=self.build_url(endpoint))

    def get_dispute(self, account_id, dispute_id):
        endpoint = FrontEndEndpoint.DISPUTE_ID.value.format(accountId=account_id, disputeId=dispute_id)
        return self.get(url=self.build_url(endpoint))

    def create_dispute(self, account_id, **request_body):
        endpoint = FrontEndEndpoint.DISPUTE_ACCOUNT_ID.value.format(accountId=account_id)
        return self.post(url=self.build_url(endpoint), json=request_body)

    def delete_dispute(self, account_id, dispute_id):
        endpoint = FrontEndEndpoint.DISPUTE_ID.value.format(accountId=account_id, disputeId=dispute_id)
        return self.delete(url=self.build_url(endpoint))

    def get_hade_history(self, account_id):
        endpoint = FrontEndEndpoint.HADE_HISTORY.value.format(accountId=account_id)
        return self.get(url=self.build_url(endpoint))
