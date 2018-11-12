from client.clients.q2_client import Q2Client
from client.endpoints.v2_endpoints import CommercialEndpoint


class CommercialClient(Q2Client):

    def get_config(self):
        endpoint = CommercialEndpoint.CONFIG.value
        return self._get(url=self._build_url(endpoint))

    def create_payment(self, payment_file):
        """need additional details for this call"""
        endpoint = CommercialEndpoint.PAYMENTS.value
        return self._post(url=self._build_url(endpoint))

    def create_ach_rule(self, ach_rule):
        """need additional details for this call"""
        endpoint = CommercialEndpoint.ACH_RULE.value
        return self._post(url=self._build_url(endpoint))

    def add_check(self, check):
        """need additional details for this call"""
        endpoint = CommercialEndpoint.ADD_CHECK.value
        return self._post(url=self._build_url(endpoint))

    def get_exception_account_list(self, vendor_id):
        endpoint = CommercialEndpoint.EXCEPTION_ACCOUNTS.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def get_exception_details(self, vendor_id, transaction_id):
        endpoint = CommercialEndpoint.EXCEPTION_DETAILS.value.format(vendorId=vendor_id, transactionId=transaction_id)
        return self._get(url=self._build_url(endpoint))

    def update_exceptions(self, exceptions):
        """need additional details for this call"""
        endpoint = CommercialEndpoint.EXCEPTIONS.value
        return self._post(url=self._build_url(endpoint))

    def get_exceptions(self, vendor_id):
        endpoint = CommercialEndpoint.EXCEPTIONS_ID.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def create_recipient(self, recipient):
        """need additional details for this call"""
        endpoint = CommercialEndpoint.RECIPIENTS.value
        return self._post(url=self._build_url(endpoint))

    def get_recipient(self, recipient_id):
        endpoint = CommercialEndpoint.RECIPIENT_ID.value.format(recipientId=recipient_id)
        return self._get(url=self._build_url(endpoint))

    def get_wires(self, **query):
        endpoint = CommercialEndpoint.WIRES.value
        query_parameters = self._copy_query_parameters()
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def create_forex_quote(self, **request_body):
        endpoint = CommercialEndpoint.WIRES_FX_RATE.value
        return self._post(url=self._build_url(endpoint), json=request_body)
