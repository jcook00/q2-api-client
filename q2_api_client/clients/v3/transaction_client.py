from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import TransactionEndpoint


class TransactionClient(BaseQ2Client):

    def retrieve_transactions(self, request_body):
        """POST /v3/transaction/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TransactionEndpoint.RETRIEVE_TRANSACTIONS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_transaction(self, transaction_id):
        """POST /v3/transaction/{id}/retrieve

        :param str transaction_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TransactionEndpoint.RETRIEVE_TRANSACTION.value.format(id=transaction_id)
        return self._post(url=self._build_url(endpoint))
