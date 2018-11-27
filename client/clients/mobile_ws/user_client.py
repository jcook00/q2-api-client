from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import UserEndpoint


class UserClient(BaseQ2Client):

    def get_users(self):
        """GET /mobilews/user

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER.value
        return self._get(url=self._build_url(endpoint))

    def create_user(self, request_body):
        """POST /mobilews/user

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_user(self, user_id):
        """GET /mobilews/user/{id}

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))

    def delete_user(self, user_id):
        """DELETE /mobilews/user/{id}

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_ID.value.format(id=user_id)
        return self._delete(url=self._build_url(endpoint))

    def update_user(self, user_id, request_body):
        """PUT /mobilews/user/{id}

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_role(self, user_id, request_body):
        """PUT /mobilews/user/role/{id}

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_ROLE_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_role_decision(self, user_id, request_body):
        """PUT /mobilews/user/role/{id}/decide

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_ROLE_DECIDE.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_status(self, user_id, request_body):
        """PUT /mobilews/user/status/{id}

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_STATUS_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_status_decision(self, user_id, request_body):
        """PUT /mobilews/user/status/{id}/decide

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_STATUS_DECIDE.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_user_profiles(self):
        """GET /mobilews/userProfile

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_PROFILE.value
        return self._get(url=self._build_url(endpoint))

    def update_user_profiles(self, request_body):
        """PUT /mobilews/userProfile

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_PROFILE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_profile_decision(self, user_id, request_body):
        """PUT /mobilews/userProfile/decide/{id}

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_PROFILE_DECIDE_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_user_profile_form(self):
        """GET /mobilews/userProfile/form

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_PROFILE_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_user_profile(self, user_id):
        """GET /mobilews/userProfile/{id}

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_PROFILE_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))

    def update_user_profile(self, user_id, request_body):
        """PUT /mobilews/userProfile/{id}

        :param str user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_PROFILE_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def create_user_agent(self, request_body):
        """POST /mobilews/useragent

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = UserEndpoint.USER_AGENT.value
        return self._post(url=self._build_url(endpoint), json=request_body)
