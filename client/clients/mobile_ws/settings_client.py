from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import SettingsEndpoint


class SettingsClient(BaseQ2Client):

    def get_account_settings(self):
        endpoint = SettingsEndpoint.ACCOUNT.value
        return self._get(url=self._build_url(endpoint))

    def update_account_settings(self, **request_body):
        endpoint = SettingsEndpoint.ACCOUNT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_challenge_code(self):
        endpoint = SettingsEndpoint.CHALLENGE_CODE.value
        return self._get(url=self._build_url(endpoint))

    def update_challenge_code(self, **request_body):
        endpoint = SettingsEndpoint.CHALLENGE_CODE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def change_login(self, **request_body):
        endpoint = SettingsEndpoint.CHANGE_LOGIN.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_estatement_settings(self):
        endpoint = SettingsEndpoint.ESTATEMENT.value
        return self._get(url=self._build_url(endpoint))

    def update_estatement_settings(self, **request_body):
        endpoint = SettingsEndpoint.ESTATEMENT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_access_code_targets(self):
        endpoint = SettingsEndpoint.MFA.value
        return self._get(url=self._build_url(endpoint))

    def create_access_code_target(self, **request_body):
        endpoint = SettingsEndpoint.MFA.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_access_code_target_form(self):
        endpoint = SettingsEndpoint.MFA_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_access_code_target(self, target_id):
        endpoint = SettingsEndpoint.MFA_ID.value.format(id=target_id)
        return self._get(url=self._build_url(endpoint))

    def delete_access_code_target(self, target_id):
        endpoint = SettingsEndpoint.MFA_ID.value.format(id=target_id)
        return self._delete(url=self._build_url(endpoint))

    def update_access_code_target(self, target_id, **request_body):
        endpoint = SettingsEndpoint.MFA_ID.value.format(id=target_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_mobile_auth_settings(self):
        endpoint = SettingsEndpoint.MOBILE_AUTH.value
        return self._get(url=self._build_url(endpoint))

    def create_mobile_auth_settings(self, **request_body):
        endpoint = SettingsEndpoint.MOBILE_AUTH.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_mobile_auth_settings(self, **request_body):
        endpoint = SettingsEndpoint.MOBILE_AUTH.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_password_policy(self):
        endpoint = SettingsEndpoint.PASSWORD_POLICY.value
        return self._get(url=self._build_url(endpoint))

    def get_security_alert_settings(self):
        endpoint = SettingsEndpoint.SECURITY_ALERT.value
        return self._get(url=self._build_url(endpoint))

    def update_security_alert_settings(self, **request_body):
        endpoint = SettingsEndpoint.SECURITY_ALERT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_text_banking_settings(self):
        endpoint = SettingsEndpoint.TEXT_BANKING.value
        return self._get(url=self._build_url(endpoint))

    def create_text_banking_settings(self, **request_body):
        endpoint = SettingsEndpoint.TEXT_BANKING.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_text_banking_settings(self, **request_body):
        endpoint = SettingsEndpoint.TEXT_BANKING.value
        return self._put(url=self._build_url(endpoint), json=request_body)
