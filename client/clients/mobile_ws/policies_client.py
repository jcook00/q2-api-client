from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import PoliciesEndpoint


class PoliciesClient(BaseQ2Client):

    def get_policies(self):
        """GET /mobilews/policies

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES.value
        return self._get(url=self._build_url(endpoint))

    def create_policy(self, request_body):
        """POST /mobilews/policies

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_hydra_policies(self):
        """GET /mobilews/policies/hydra

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES_HYDRA.value
        return self._get(url=self._build_url(endpoint))

    def create_hydra_policy(self, request_body):
        """POST /mobilews/policies/hydra

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES_HYDRA.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_user_role(self):
        """GET /mobilews/policies/userrole

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES_USER_ROLE.value
        return self._get(url=self._build_url(endpoint))

    def get_users(self):
        """GET /mobilews/policies/users

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES_USERS.value
        return self._get(url=self._build_url(endpoint))

    def get_policy(self, policy_id):
        """GET /mobilews/policies/{id}

        :param str policy_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES_ID.value.format(id=policy_id)
        return self._get(url=self._build_url(endpoint))

    def delete_policy(self, policy_id):
        """DELETE /mobilews/policies/{id}

        :param str policy_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES_ID.value.format(id=policy_id)
        return self._delete(url=self._build_url(endpoint))

    def update_policy(self, policy_id, request_body):
        """PUT /mobilews/policies/{id}

        :param str policy_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES_ID.value.format(id=policy_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def approve_policy(self, policy_id, request_body):
        """PUT /mobilews/policies/{id}/approve

        :param str policy_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICIES_APPROVE.value.format(id=policy_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_policy_features(self):
        """GET /mobilews/policyFeatures

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICY_FEATURES.value
        return self._get(url=self._build_url(endpoint))

    def get_company_policy_set(self):
        """GET /mobilews/policySet/company

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICY_SET_COMPANY.value
        return self._get(url=self._build_url(endpoint))

    def create_hydra_policy_set(self, request_body):
        """POST /mobilews/policySet/hydra

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICY_SET_HYDRA.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_user_policy_set(self):
        """GET /mobilews/policySet/user

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICY_SET_USER.value
        return self._get(url=self._build_url(endpoint))

    def get_policy_set(self, policy_set_id):
        """GET /mobilews/policySet/{id}

        :param str policy_set_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = PoliciesEndpoint.POLICY_SET_ID.value.format(id=policy_set_id)
        return self._get(url=self._build_url(endpoint))
