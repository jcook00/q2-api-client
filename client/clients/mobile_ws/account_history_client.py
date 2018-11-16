from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AccountHistoryEndpoint


class AccountHistoryClient(BaseQ2Client):

    def get_account_history(self, account_id):
        endpoint = AccountHistoryEndpoint.ACCOUNT_HISTORY_ID.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_inquiry_link_history_template(self, account_id, transaction_id, transaction_type):
        endpoint = AccountHistoryEndpoint.INQUIRY_LINK.value.format(id=account_id, transactionId=transaction_id,
                                                                    type=transaction_type)
        return self._get(url=self._build_url(endpoint))

    def create_inquiry_link_history_template(self, account_id, transaction_id, transaction_type, **request_body):
        endpoint = AccountHistoryEndpoint.INQUIRY_LINK.value.format(id=account_id, transactionId=transaction_id,
                                                                    type=transaction_type)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_account_history_detail_image(self, account_id, transaction_id, sequence_id):
        endpoint = AccountHistoryEndpoint.IMAGE_SEQUENCE_ID.value.format(id=account_id, transactionId=transaction_id,
                                                                         sequenceId=sequence_id)
        return self._get(url=self._build_url(endpoint))

    def get_account_history_detail(self, account_id, transaction_id, transaction_type):
        endpoint = AccountHistoryEndpoint.DETAIL_TRANSACTION_TYPE.value.format(id=account_id,
                                                                               transactionId=transaction_id,
                                                                               transactionType=transaction_type)
        return self._get(url=self._build_url(endpoint))

    def get_account_history_images(self, account_id, transaction_id, transaction_type):
        endpoint = AccountHistoryEndpoint.IMAGE_TRANSACTION_TYPE.value.format(id=account_id,
                                                                              transactionId=transaction_id,
                                                                              transactionType=transaction_type)
        return self._get(url=self._build_url(endpoint))

    def get_account_history_image(self, account_id, transaction_id, transaction_type, image_number):
        endpoint = AccountHistoryEndpoint.IMAGE_NUMBER.value.format(id=account_id, transactionId=transaction_id,
                                                                    transactionType=transaction_type,
                                                                    imageNumber=image_number)
        return self._get(url=self._build_url(endpoint))
