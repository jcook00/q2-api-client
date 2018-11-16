from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import UserEndpoint


class UserClient(BaseQ2Client):

    def get_users(self):
        endpoint = UserEndpoint.USER.value
        return self._get(url=self._build_url(endpoint))

    def create_user(self, **request_body):
        endpoint = UserEndpoint.USER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_user(self, user_id):
        endpoint = UserEndpoint.USER_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))

    def delete_user(self, user_id):
        endpoint = UserEndpoint.USER_ID.value.format(id=user_id)
        return self._delete(url=self._build_url(endpoint))

    def update_user(self, user_id, **request_body):
        endpoint = UserEndpoint.USER_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_role(self, user_id, **request_body):
        endpoint = UserEndpoint.USER_ROLE_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_role_decision(self, user_id, **request_body):
        endpoint = UserEndpoint.USER_ROLE_DECIDE.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_status(self, user_id, **request_body):
        endpoint = UserEndpoint.USER_STATUS_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_status_decision(self, user_id, **request_body):
        endpoint = UserEndpoint.USER_STATUS_DECIDE.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_user_profiles(self):
        endpoint = UserEndpoint.USER_PROFILE.value
        return self._get(url=self._build_url(endpoint))

    def update_user_profiles(self, **request_body):
        endpoint = UserEndpoint.USER_PROFILE.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_user_profile_decision(self, user_id, **request_body):
        endpoint = UserEndpoint.USER_PROFILE_DECIDE_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_user_profile_form(self):
        endpoint = UserEndpoint.USER_PROFILE_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_user_profile(self, user_id):
        endpoint = UserEndpoint.USER_PROFILE_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))

    def update_user_profile(self, user_id, **request_body):
        endpoint = UserEndpoint.USER_PROFILE_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def create_user_agent(self, **request_body):
        endpoint = UserEndpoint.USER_AGENT.value
        return self._post(url=self._build_url(endpoint), json=request_body)
