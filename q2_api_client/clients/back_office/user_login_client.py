from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import UserLoginEndpoint


class UserLoginClient(BaseQ2Client):

    def retrieve_user_logins(self, request_body):
        """POST /backoffice/v3/userLogin/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserLoginEndpoint.RETRIEVE_USER_LOGINS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_user_login(self, user_id):
        """POST /backoffice/v3/userLogin/{id}/retrieve

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserLoginEndpoint.RETRIEVE_USER_LOGIN.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint))

    def patch_user_login(self, user_id, request_body):
        """POST /backoffice/v3/userLogin/{id}/patch

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserLoginEndpoint.PATCH_USER_LOGIN.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_user_login(self, user_id, request_body):
        """POST /backoffice/v3/userLogin/{id}/update

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserLoginEndpoint.UPDATE_USER_LOGIN.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def reset_device_registration(self, user_id):
        """POST /backoffice/v3/userLogin/{id}/resetDeviceRegistration

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserLoginEndpoint.RESET_DEVICE_REGISTRATION.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint))

    def restore_user_login(self, user_id, request_body):
        """POST /backoffice/v3/userLogin/{id}/restore

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserLoginEndpoint.RESTORE_USER_LOGIN.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def change_user_password(self, user_id, request_body):
        """POST /backoffice/v3/userLogin/{id}/changePassword

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserLoginEndpoint.CHANGE_PASSWORD.value.format(id=user_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
