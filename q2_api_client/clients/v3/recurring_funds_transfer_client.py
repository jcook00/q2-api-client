from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import RecurringFundsTransferEndpoint


class RecurringFundsTransferClient(BaseQ2Client):

    def get_recurring_funds_transfer_permission(self):
        """GET /v3/recurringFundsTransfer/permission

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RecurringFundsTransferEndpoint.RECURRING_FUNDS_TRANSFER_PERMISSIONS.value
        return self._get(url=self._build_url(endpoint))

    def create_recurring_funds_transfer(self, request_body):
        """POST /v3/recurringFundsTransfer/create

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RecurringFundsTransferEndpoint.CREATE_RECURRING_FUNDS_TRANSFER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_recurring_funds_transfers(self, request_body):
        """POST /v3/recurringFundsTransfer/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RecurringFundsTransferEndpoint.RETRIEVE_RECURRING_FUNDS_TRANSFERS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_recurring_funds_transfer(self, transfer_id):
        """POST /v3/recurringFundsTransfer/{id}/retrieve

        :param str transfer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RecurringFundsTransferEndpoint.RETRIEVE_RECURRING_FUNDS_TRANSFER.value.format(id=transfer_id)
        return self._post(url=self._build_url(endpoint))

    def cancel_recurring_funds_transfer(self, transfer_id):
        """POST /v3/recurringFundsTransfer/{id}/cancel

        :param str transfer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RecurringFundsTransferEndpoint.CANCEL_RECURRING_FUNDS_TRANSFER.value.format(id=transfer_id)
        return self._post(url=self._build_url(endpoint))

    def authorize_recurring_funds_transfer(self, transfer_id):
        """POST /v3/recurringFundsTransfer/{id}/authorize

        :param str transfer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RecurringFundsTransferEndpoint.AUTHORIZE_RECURRING_FUNDS_TRANSFER.value.format(id=transfer_id)
        return self._post(url=self._build_url(endpoint))
