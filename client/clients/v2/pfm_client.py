from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.v2_endpoints import PFMEndpoint


class PFMClient(BaseQ2Client):

    def get_account(self, account_guid, member_guid=None):
        """GET /v2/pfm/accounts/{accountGuid}

        :param str account_guid: path parameter
        :param str member_guid: query parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.ACCOUNT_GUID.value.format(accountGuid=account_guid)
        query_parameters = self._copy_query_parameters()
        query_parameters['member_guid'] = member_guid
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def update_account(self, account_guid, request_body):
        """PUT /v2/pfm/accounts/{accountGuid}

        :param str account_guid: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.ACCOUNT_GUID.value.format(accountGuid=account_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_categories(self):
        """GET /v2/pfm/categories

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.CATEGORIES.value
        return self._get(url=self._build_url(endpoint))

    def create_category(self, request_body):
        """POST /v2/pfm/categories

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.CATEGORIES.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_category(self, category_guid):
        """DELETE /v2/pfm/categories/{categoryGuid}

        :param str category_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.CATEGORY_GUID.value.format(categoryGuid=category_guid)
        return self._delete(url=self._build_url(endpoint))

    def update_category(self, category_guid, request_body):
        """PUT /v2/pfm/categories/{categoryGuid}

        :param str category_guid: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.CATEGORY_GUID.value.format(categoryGuid=category_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_institutions(self, name=None, count=None):
        """GET /v2/pfm/institutions

        :param str name: query parameter (string to search the institution names by)
        :param int count: query parameter (number of results to return)
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.INSTITUTIONS.value
        query_parameters = self._copy_query_parameters()
        query_parameters['name'] = name
        query_parameters['count'] = count
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def get_institution(self, institution_guid):
        """GET /v2/pfm/institutions/{institutionGuid}

        :param str institution_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.INSTITUTION_GUID.value.format(institutionGuid=institution_guid)
        return self._get(url=self._build_url(endpoint))

    def get_institution_credentials(self, institution_guid):
        """GET /v2/pfm/institutions/{institutionGuid}/credentials

        :param str institution_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.INSTITUTION_CREDENTIALS.value.format(institutionGuid=institution_guid)
        return self._get(url=self._build_url(endpoint))

    def get_job(self, job_guid):
        """GET /v2/pfm/jobs/{jobGuid}

        :param str job_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.JOB.value.format(jobGuid=job_guid)
        return self._get(url=self._build_url(endpoint))

    def get_job_mfa_credentials(self, job_guid):
        """GET /v2/pfm/jobs/{jobGuid}/mfa_credentials

        :param str job_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.JOB_MFA_CREDENTIALS.value.format(jobGuid=job_guid)
        return self._get(url=self._build_url(endpoint))

    def resume_job(self, job_guid):
        """POST /v2/pfm/jobs/{jobGuid}/resume

        :param str job_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.JOB_RESUME.value.format(jobGuid=job_guid)
        return self._post(url=self._build_url(endpoint))

    def get_member(self, member_guid):
        """GET /v2/pfm/members/{memberGuid}

        :param str member_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.MEMBER_GUID.value.format(memberGuid=member_guid)
        return self._get(url=self._build_url(endpoint))

    def create_member(self, request_body):
        """POST /v2/pfm/members/

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.MEMBERS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_member(self, member_guid, request_body):
        """PUT /v2/pfm/members/{memberGuid}

        :param str member_guid: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.MEMBER_GUID.value.format(memberGuid=member_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_member(self, member_guid):
        """DELETE /v2/pfm/members/{memberGuid}

        :param str member_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.MEMBER_GUID.value.format(memberGuid=member_guid)
        return self._delete(url=self._build_url(endpoint))

    def delete_all_members(self):
        """DELETE /v2/pfm/members/all

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.ALL_MEMBERS.value
        return self._delete(url=self._build_url(endpoint))

    def create_member_credentials(self, member_guid, request_body):
        """POST /v2/pfm/members/{memberGuid}/credentials

        :param str member_guid: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.MEMBER_CREDENTIALS.value.format(memberGuid=member_guid)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def refresh_member(self, member_guid):
        """POST /v2/pfm/members/{memberGuid}/refresh

        :param str member_guid: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.MEMBER_REFRESH.value.format(memberGuid=member_guid)
        return self._post(url=self._build_url(endpoint))

    def update_transaction(self, transaction_guid, request_body):
        """PUT /v2/pfm/transactions/{transactionGuid}

        :param str transaction_guid: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.TRANSACTION_GUID.value.format(transactionGuid=transaction_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_split_transaction(self, transaction_guid, request_body):
        """PUT /v2/pfm/transactions/{transactionGuid}/splits

        :param str transaction_guid: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.TRANSACTION_SPLITS.value.format(transactionGuid=transaction_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def create_user(self):
        """POST /v2/pfm/users

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.USERS.value
        return self._post(url=self._build_url(endpoint))

    def get_widget(self, widget_short_name, no_redirect=None, q2token=None):
        """GET /v2/pfm/widgets/{widgetShortName}

        :param str widget_short_name: path parameter
        :param bool no_redirect: query parameter
            (Flag to return url data and not send a 302 redirect)
        :param str q2token: query parameter
            (Allow passing in q2token by query string for authentication)
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PFMEndpoint.WIDGET.value.format(widgetShortName=widget_short_name)
        query_parameters = self._copy_query_parameters()
        query_parameters['no_redirect'] = no_redirect
        query_parameters['q2token'] = q2token
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)
