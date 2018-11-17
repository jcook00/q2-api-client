from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import PreLogonEndpoint


class PreLogonClient(BaseQ2Client):

    def pre_logon_user(self):
        endpoint = PreLogonEndpoint.PRE_LOGON_USER.value
        return self._get(url=self._build_url(endpoint))

    def trigger_pre_logon_user(self, **request_body):
        endpoint = PreLogonEndpoint.PRE_LOGON_USER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def pre_logon_user_clear_cache(self):
        endpoint = PreLogonEndpoint.PRE_LOGON_USER_CLEAR_CACHE.value
        return self._get(url=self._build_url(endpoint))
