from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AccountEndpoint


class AccountClient(BaseQ2Client):

    def get_accounts(self):
        endpoint = AccountEndpoint.ACCOUNT.value
        return self._get(url=self._build_url(endpoint))

    def set_pfm_enrollment_to_true(self):
        endpoint = AccountEndpoint.ACCOUNT_SET_ENROLLED.value
        return self._get(url=self._build_url(endpoint))

    def get_account_groups(self):
        endpoint = AccountEndpoint.ACCOUNT_GROUP.value
        return self._get(url=self._build_url(endpoint))

    def create_account_group(self, **request_body):
        endpoint = AccountEndpoint.ACCOUNT_GROUP.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_account_group(self, group_id):
        endpoint = AccountEndpoint.ACCOUNT_GROUP_ID.value.format(id=group_id)
        return self._delete(url=self._build_url(endpoint))

    def update_account_group(self, group_id, **request_body):
        endpoint = AccountEndpoint.ACCOUNT_GROUP_ID.value.format(id=group_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_account_labels(self):
        endpoint = AccountEndpoint.ACCOUNT_LABEL.value
        return self._get(url=self._build_url(endpoint))

    def create_account_label(self, **request_body):
        endpoint = AccountEndpoint.ACCOUNT_LABEL.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_account_label(self, label_id):
        endpoint = AccountEndpoint.ACCOUNT_LABEL_ID.value.format(id=label_id)
        return self._delete(url=self._build_url(endpoint))

    def update_account_label(self, label_id, **request_body):
        endpoint = AccountEndpoint.ACCOUNT_LABEL_ID.value.format(id=label_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_inquiry_link_history_template(self, account_id):
        endpoint = AccountEndpoint.ACCOUNT_INQUIRY_LINK.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def create_inquiry_link_history_template(self, account_id, **request_body):
        endpoint = AccountEndpoint.ACCOUNT_INQUIRY_LINK.value.format(id=account_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_account(self, account_id):
        endpoint = AccountEndpoint.ACCOUNT_ID.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def create_account(self, account_id, **request_body):
        endpoint = AccountEndpoint.ACCOUNT_ID.value.format(id=account_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_account(self, account_id):
        endpoint = AccountEndpoint.ACCOUNT_ID.value.format(id=account_id)
        return self._delete(url=self._build_url(endpoint))

    def update_account(self, account_id, **request_body):
        endpoint = AccountEndpoint.ACCOUNT_ID.value.format(id=account_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_account_detail_click_value(self, account_id, hade_id):
        endpoint = AccountEndpoint.ACCOUNT_HADE_ID.value.format(id=account_id, hadeId=hade_id)
        return self._get(url=self._build_url(endpoint))
