from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import FormEndpoint


class FormClient(BaseQ2Client):

    def get_forms(self):
        endpoint = FormEndpoint.FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_form(self, form_id):
        endpoint = FormEndpoint.FORM_ID.value.format(id=form_id)
        return self._get(url=self._build_url(endpoint))

    def set_form(self, form_id, **request_body):
        endpoint = FormEndpoint.FORM_ID.value.format(id=form_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_account_form(self, form_id, account_id):
        endpoint = FormEndpoint.FORM_ACCOUNT_ID.value.format(id=form_id, accountId=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_account_hade_form(self, form_id, account_id, hade_id):
        endpoint = FormEndpoint.FORM_HADE_ID.value.format(id=form_id, accountId=account_id, hadeid=hade_id)
        return self._get(url=self._build_url(endpoint))

    def get_form_unauth(self, form_id):
        endpoint = FormEndpoint.FORM_UNAUTH.value.format(id=form_id)
        return self._get(url=self._build_url(endpoint))

    def set_form_unauth(self, form_id, **request_body):
        endpoint = FormEndpoint.FORM_UNAUTH.value.format(id=form_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
