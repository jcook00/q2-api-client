from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import TransactionDetailEndpoint


class TransactionDetailClient(BaseQ2Client):

    def retrieve_transaction_details(self, request_body):
        """POST /v3/transactionDetail/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TransactionDetailEndpoint.RETRIEVE_TRANSACTION_DETAILS.value
        return self._post(url=self._build_url(endpoint), json=request_body)
