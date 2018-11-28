from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import AccountEndpoint


class AccountClient(BaseQ2Client):

    def get_accounts(self):
        """GET /mobilews/account

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT.value
        return self._get(url=self._build_url(endpoint))

    def set_pfm_enrollment_to_true(self):
        """GET /mobilews/account/Pfm/setEnrolledToTrue

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_SET_ENROLLED.value
        return self._get(url=self._build_url(endpoint))

    def get_account_groups(self):
        """GET /mobilews/account/group

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_GROUP.value
        return self._get(url=self._build_url(endpoint))

    def create_account_group(self, request_body):
        """POST /mobilews/account/group

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_GROUP.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_account_group(self, group_id):
        """DELETE /mobilews/account/group/{id}

        :param str group_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_GROUP_ID.value.format(id=group_id)
        return self._delete(url=self._build_url(endpoint))

    def update_account_group(self, group_id, request_body):
        """PUT /mobilews/account/group/{id}

        :param str group_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_GROUP_ID.value.format(id=group_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_account_labels(self):
        """GET /mobilews/account/label

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_LABEL.value
        return self._get(url=self._build_url(endpoint))

    def create_account_label(self, request_body):
        """POST /mobilews/account/label

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_LABEL.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_account_label(self, label_id):
        """DELETE /mobilews/account/label/{id}

        :param str label_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_LABEL_ID.value.format(id=label_id)
        return self._delete(url=self._build_url(endpoint))

    def update_account_label(self, label_id, request_body):
        """PUT /mobilews/account/label/{id}

        :param str label_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_LABEL_ID.value.format(id=label_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_inquiry_link_history_template(self, account_id):
        """GET /mobilews/account/{id}/inquiryLink

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_INQUIRY_LINK.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def create_inquiry_link_history_template(self, account_id, request_body):
        """POST /mobilews/account/{id}/inquiryLink

        :param str account_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_INQUIRY_LINK.value.format(id=account_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_account(self, account_id):
        """GET /mobilews/account/{id}

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_ID.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def create_account(self, account_id, request_body):
        """POST /mobilews/account/{id}

        :param str account_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_ID.value.format(id=account_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_account(self, account_id):
        """DELETE /mobilews/account/{id}

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_ID.value.format(id=account_id)
        return self._delete(url=self._build_url(endpoint))

    def update_account(self, account_id, request_body):
        """PUT /mobilews/account/{id}

        :param str account_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_ID.value.format(id=account_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_account_detail_click_value(self, account_id, hade_id):
        """GET /mobilews/account/{id}/{hadeId}

        :param str account_id: path parameter
        :param str hade_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountEndpoint.ACCOUNT_HADE_ID.value.format(id=account_id, hadeId=hade_id)
        return self._get(url=self._build_url(endpoint))
