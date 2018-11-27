from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import SettingsEndpoint


class SettingsClient(BaseQ2Client):

    def get_account_settings(self):
        """GET /mobilews/settings/account

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.ACCOUNT.value
        return self._get(url=self._build_url(endpoint))

    def update_account_settings(self, request_body):
        """PUT /mobilews/settings/account

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.ACCOUNT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_challenge_code(self):
        """GET /mobilews/settings/challengeCode

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.CHALLENGE_CODE.value
        return self._get(url=self._build_url(endpoint))

    def update_challenge_code(self, request_body):
        """PUT /mobilews/settings/challengeCode

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.CHALLENGE_CODE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def change_login(self, request_body):
        """PUT /mobilews/settings/changeLogin

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.CHANGE_LOGIN.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_estatement_settings(self):
        """GET /mobilews/settings/estatement

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.ESTATEMENT.value
        return self._get(url=self._build_url(endpoint))

    def update_estatement_settings(self, request_body):
        """PUT /mobilews/settings/estatement

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.ESTATEMENT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_access_code_targets(self):
        """GET /mobilews/settings/mfa

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MFA.value
        return self._get(url=self._build_url(endpoint))

    def create_access_code_target(self, request_body):
        """POST /mobilews/settings/mfa

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MFA.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_access_code_target_form(self):
        """GET /mobilews/settings/mfa/form

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MFA_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_access_code_target(self, target_id):
        """GET /mobilews/settings/mfa/{id}

        :param str target_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MFA_ID.value.format(id=target_id)
        return self._get(url=self._build_url(endpoint))

    def delete_access_code_target(self, target_id):
        """DELETE /mobilews/settings/mfa/{id}

        :param str target_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MFA_ID.value.format(id=target_id)
        return self._delete(url=self._build_url(endpoint))

    def update_access_code_target(self, target_id, request_body):
        """PUT /mobilews/settings/mfa/{id}

        :param str target_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MFA_ID.value.format(id=target_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_mobile_auth_settings(self):
        """GET /mobilews/settings/mobileAuth

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MOBILE_AUTH.value
        return self._get(url=self._build_url(endpoint))

    def create_mobile_auth_settings(self, request_body):
        """POST /mobilews/settings/mobileAuth

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MOBILE_AUTH.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_mobile_auth_settings(self, request_body):
        """PUT /mobilews/settings/mobileAuth

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.MOBILE_AUTH.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_password_policy(self):
        """GET /mobilews/settings/passwordPolicy

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.PASSWORD_POLICY.value
        return self._get(url=self._build_url(endpoint))

    def get_security_alert_settings(self):
        """GET /mobilews/settings/securityAlert

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.SECURITY_ALERT.value
        return self._get(url=self._build_url(endpoint))

    def update_security_alert_settings(self, request_body):
        """PUT /mobilews/settings/securityAlert

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.SECURITY_ALERT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_text_banking_settings(self):
        """GET /mobilews/settings/textbanking

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.TEXT_BANKING.value
        return self._get(url=self._build_url(endpoint))

    def create_text_banking_settings(self, request_body):
        """POST /mobilews/settings/textbanking

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.TEXT_BANKING.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_text_banking_settings(self, request_body):
        """PUT /mobilews/settings/textbanking

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SettingsEndpoint.TEXT_BANKING.value
        return self._put(url=self._build_url(endpoint), json=request_body)
