from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import UserEndpoint


class UserClient(BaseQ2Client):

    def retrieve_users(self, request_body):
        """POST /backoffice/v3/user/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_USERS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_user(self, user_id, request_body):
        """POST /backoffice/v3/user/{id}/account/retrieve

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_USER.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_user(self, user_id, request_body):
        """POST /backoffice/v3/user/{id}/update

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.UPDATE_USER.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_phone_number(self, user_id, request_body):
        """POST /backoffice/v3/user/{id}/phone/create

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.CREATE_PHONE.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_phone_numbers(self, user_id):
        """POST /backoffice/v3/user/{id}/phone/retrieve

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_PHONE.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint))

    def retrieve_user_logins(self, user_id):
        """POST /backoffice/v3/user/{id}/userLogin/retrieve

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_USER_LOGIN.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint))

    def retrieve_csr_assist_policy(self, user_id):
        """POST /backoffice/v3/user/{id}/csrAssistPolicy/retrieve

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_CSR_ASSIST_POLICY.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint))

    def retrieve_user_accounts(self, user_id, request_body):
        """POST /backoffice/v3/user/{id}/account/retrieve

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_USER_ACCOUNT.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_feature_rights(self, user_id):
        """POST /backoffice/v3/user/{id}/featureRight/retrieve

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.RETRIEVE_FEATURE_RIGHT.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint))

    def delete_phone_numbers(self, user_id, phone_id):
        """POST /backoffice/v3/user/{id}/phone/{phoneId}/delete

        :param str user_id: path parameter
        :param str phone_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.DELETE_PHONE.value.format(id=user_id, phoneId=phone_id)
        return self._post(url=self._build_url(endpoint))

    def update_phone_numbers(self, user_id, phone_id, request_body):
        """POST /backoffice/v3/user/{id}/phone/{phoneId}/delete

        :param str user_id: path parameter
        :param str phone_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.UPDATE_PHONE.value.format(id=user_id, phoneId=phone_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
