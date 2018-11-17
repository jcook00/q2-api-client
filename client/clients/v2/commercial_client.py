from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.v2_endpoints import CommercialEndpoint


class CommercialClient(BaseQ2Client):

    def get_config(self):
        """GET /v2/commercial/config

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.CONFIG.value
        return self._get(url=self._build_url(endpoint))

    def create_payment(self, payment_file):
        """POST /v2/commercial/payments
        need additional details for this call

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.PAYMENTS.value
        return self._post(url=self._build_url(endpoint))

    def create_ach_rule(self, ach_rule):
        """POST /v2/commercial/positive-pay/ach-rule
        need additional details for this call

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.ACH_RULE.value
        return self._post(url=self._build_url(endpoint))

    def add_check(self, check):
        """POST /v2/commercial/positive-pay/add-check
        need additional details for this call

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.ADD_CHECK.value
        return self._post(url=self._build_url(endpoint))

    def get_exception_account_list(self, vendor_id):
        """GET /v2/commercial/positive-pay/exception-accounts/{vendorId}

        :param int vendor_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.EXCEPTION_ACCOUNTS.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def get_exception_details(self, vendor_id, transaction_id):
        """GET /v2/commercial/positive-pay/exception-details/{vendorId}/{transactionId}

        :param int vendor_id: path parameter
        :param int transaction_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.EXCEPTION_DETAILS.value.format(vendorId=vendor_id, transactionId=transaction_id)
        return self._get(url=self._build_url(endpoint))

    def update_exceptions(self, exceptions):
        """POST /v2/commercial/positive-pay/exceptions
        need additional details for this call

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.EXCEPTIONS.value
        return self._post(url=self._build_url(endpoint))

    def get_exceptions(self, vendor_id):
        """GET /v2/commercial/positive-pay/exceptions/{vendorId}

        :param int vendor_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.EXCEPTIONS_ID.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def create_recipient(self, recipient):
        """POST /v2/commercial/recipients
        need additional details for this call

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENTS.value
        return self._post(url=self._build_url(endpoint))

    def get_recipient(self, recipient_id):
        """GET /v2/commercial/recipients/{recipientId}

        :param int recipient_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_ID.value.format(recipientId=recipient_id)
        return self._get(url=self._build_url(endpoint))

    def get_wires(self, **query):
        """GET /v2/commercial/wires

        :param dict query: query parameters
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.WIRES.value
        query_parameters = self._copy_query_parameters()
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def create_forex_quote(self, request_body):
        """POST /v2/commercial/wires/fx-rate

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.WIRES_FX_RATE.value
        return self._post(url=self._build_url(endpoint), json=request_body)
