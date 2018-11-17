from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import TransactionEndpoint


class TransactionClient(BaseQ2Client):

    def approve_multi_recurring_transactions(self, **request_body):
        endpoint = TransactionEndpoint.TRANSACTION_APPROVE_MULTI_RECURRING.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_transactions(self, **request_body):
        endpoint = TransactionEndpoint.TRANSACTION_MULTI.value
        return self._delete(url=self._build_url(endpoint), json=request_body)

    def authorize_transactions(self, **request_body):
        endpoint = TransactionEndpoint.TRANSACTION_MULTI.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_transaction(self, transaction_id):
        endpoint = TransactionEndpoint.TRANSACTION_ID.value.format(id=transaction_id)
        return self._get(url=self._build_url(endpoint))

    def authorize_transaction(self, transaction_id, **request_body):
        endpoint = TransactionEndpoint.TRANSACTION_ID.value.format(id=transaction_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_transaction_inquiry_link(self, transaction_id):
        endpoint = TransactionEndpoint.TRANSACTION_INQUIRY_LINK.value.format(id=transaction_id)
        return self._get(url=self._build_url(endpoint))

    def create_transaction_inquiry_link(self, transaction_id, **request_body):
        endpoint = TransactionEndpoint.TRANSACTION_INQUIRY_LINK.value.format(id=transaction_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def request_transaction_notification(self, transaction_id, **request_body):
        endpoint = TransactionEndpoint.TRANSACTION_NOTIFY.value.format(transactionId=transaction_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def request_transaction_notification_batch(self, transaction_id, **request_body):
        endpoint = TransactionEndpoint.TRANSACTION_NOTIFY_BATCH.value.format(transactionId=transaction_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_transaction(self, transaction_type, **request_body):
        endpoint = TransactionEndpoint.TRANSACTION_TYPE.value.format(type=transaction_type)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_transaction_form(self, transaction_type):
        endpoint = TransactionEndpoint.TRANSACTION_FORM.value.format(type=transaction_type)
        return self._get(url=self._build_url(endpoint))

    def get_transactions(self):
        endpoint = TransactionEndpoint.TRANSACTIONS.value
        return self._get(url=self._build_url(endpoint))

    def get_transactions_columns(self):
        endpoint = TransactionEndpoint.TRANSACTIONS_COLUMNS.value
        return self._get(url=self._build_url(endpoint))

    def get_pending_transactions(self):
        endpoint = TransactionEndpoint.TRANSACTIONS_PENDING.value
        return self._get(url=self._build_url(endpoint))

    def get_only_dual_pending_transactions(self, only_dual):
        endpoint = TransactionEndpoint.TRANSACTIONS_PENDING_ONLY_DUAL.value.format(onlyDual=only_dual)
        return self._get(url=self._build_url(endpoint))

    def get_recurring_transactions(self):
        endpoint = TransactionEndpoint.TRANSACTIONS_RECURRING.value
        return self._get(url=self._build_url(endpoint))

    def get_recurring_transaction(self, transaction_id):
        endpoint = TransactionEndpoint.TRANSACTIONS_RECURRING_ID.value.format(id=transaction_id)
        return self._get(url=self._build_url(endpoint))

    def delete_recurring_transaction(self, transaction_id):
        endpoint = TransactionEndpoint.TRANSACTIONS_RECURRING_ID.value.format(id=transaction_id)
        return self._delete(url=self._build_url(endpoint))
