from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import FormEndpoint


class FormClient(BaseQ2Client):

    def get_forms(self):
        """GET /mobilews/form

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FormEndpoint.FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_form(self, form_id):
        """GET /mobilews/form/{id}

        :param str form_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FormEndpoint.FORM_ID.value.format(id=form_id)
        return self._get(url=self._build_url(endpoint))

    def set_form(self, form_id, request_body):
        """POST /mobilews/form/{id}

        :param str form_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FormEndpoint.FORM_ID.value.format(id=form_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_account_form(self, form_id, account_id):
        """GET /mobilews/form/{id}/{accountId}

        :param str form_id: path parameter
        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FormEndpoint.FORM_ACCOUNT_ID.value.format(id=form_id, accountId=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_account_hade_form(self, form_id, account_id, hade_id):
        """GET /mobilews/form/{id}/{accountId}/{hadeid}

        :param str form_id: path parameter
        :param str account_id: path parameter
        :param str hade_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FormEndpoint.FORM_HADE_ID.value.format(id=form_id, accountId=account_id, hadeid=hade_id)
        return self._get(url=self._build_url(endpoint))

    def get_form_unauth(self, form_id):
        """GET /mobilews/formUnauth/{id}

        :param str form_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FormEndpoint.FORM_UNAUTH.value.format(id=form_id)
        return self._get(url=self._build_url(endpoint))

    def set_form_unauth(self, form_id, request_body):
        """POST /mobilews/formUnauth/{id}

        :param str form_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FormEndpoint.FORM_UNAUTH.value.format(id=form_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
