from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import PoliciesEndpoint


class PoliciesClient(BaseQ2Client):

    def get_policies(self):
        endpoint = PoliciesEndpoint.POLICIES.value
        return self._get(url=self._build_url(endpoint))

    def create_policy(self, **request_body):
        endpoint = PoliciesEndpoint.POLICIES.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_hydra_policies(self):
        endpoint = PoliciesEndpoint.POLICIES_HYDRA.value
        return self._get(url=self._build_url(endpoint))

    def create_hydra_policy(self, **request_body):
        endpoint = PoliciesEndpoint.POLICIES_HYDRA.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_user_role(self):
        endpoint = PoliciesEndpoint.POLICIES_USER_ROLE.value
        return self._get(url=self._build_url(endpoint))

    def get_users(self):
        endpoint = PoliciesEndpoint.POLICIES_USERS.value
        return self._get(url=self._build_url(endpoint))

    def get_policy(self, policy_id):
        endpoint = PoliciesEndpoint.POLICIES_ID.value.format(id=policy_id)
        return self._get(url=self._build_url(endpoint))

    def delete_policy(self, policy_id):
        endpoint = PoliciesEndpoint.POLICIES_ID.value.format(id=policy_id)
        return self._delete(url=self._build_url(endpoint))

    def update_policy(self, policy_id, **request_body):
        endpoint = PoliciesEndpoint.POLICIES_ID.value.format(id=policy_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def approve_policy(self, policy_id, **request_body):
        endpoint = PoliciesEndpoint.POLICIES_APPROVE.value.format(id=policy_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_policy_features(self):
        endpoint = PoliciesEndpoint.POLICY_FEATURES.value
        return self._get(url=self._build_url(endpoint))

    def get_company_policy_set(self):
        endpoint = PoliciesEndpoint.POLICY_SET_COMPANY.value
        return self._get(url=self._build_url(endpoint))

    def create_hydra_policy_set(self, **request_body):
        endpoint = PoliciesEndpoint.POLICY_SET_HYDRA.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_user_policy_set(self):
        endpoint = PoliciesEndpoint.POLICY_SET_USER.value
        return self._get(url=self._build_url(endpoint))

    def get_policy_set(self, policy_set_id):
        endpoint = PoliciesEndpoint.POLICY_SET_ID.value.format(id=policy_set_id)
        return self._get(url=self._build_url(endpoint))
