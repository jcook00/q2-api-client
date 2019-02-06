from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import FundsTransferEndpoint


class FundsTransferClient(BaseQ2Client):

    def get_funds_transfer_permission(self):
        """GET /v3/fundsTransfer/permission

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FundsTransferEndpoint.FUNDS_TRANSFER_PERMISSION.value
        return self._get(url=self._build_url(endpoint))

    def create_funds_transfer(self, request_body):
        """POST /v3/fundsTransfer/create

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FundsTransferEndpoint.CREATE_FUNDS_TRANSFER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_funds_transfers(self, request_body):
        """POST /v3/fundsTransfer/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FundsTransferEndpoint.RETRIEVE_FUNDS_TRANSFERS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_funds_transfer(self, transfer_id):
        """POST /v3/fundsTransfer/{id}/retrieve

        :param str transfer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FundsTransferEndpoint.RETRIEVE_FUNDS_TRANSFER.value.format(id=transfer_id)
        return self._post(url=self._build_url(endpoint))

    def cancel_funds_transfer(self, transfer_id):
        """POST /v3/fundsTransfer/{id}/cancel

        :param str transfer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FundsTransferEndpoint.CANCEL_FUNDS_TRANSFER.value.format(id=transfer_id)
        return self._post(url=self._build_url(endpoint))

    def authorize_funds_transfer(self, transfer_id):
        """POST /v3/fundsTransfer/{id}/authorize

        :param str transfer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FundsTransferEndpoint.AUTHORIZE_FUNDS_TRANSFER.value.format(id=transfer_id)
        return self._post(url=self._build_url(endpoint))
