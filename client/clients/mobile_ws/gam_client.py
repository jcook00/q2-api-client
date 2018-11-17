from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import GAMEndpoint


class GAMClient(BaseQ2Client):

    def get_gam_lookup_tables(self):
        endpoint = GAMEndpoint.LOOKUP.value
        return self._get(url=self._build_url(endpoint))

    def get_gam_teams(self):
        endpoint = GAMEndpoint.TEAM.value
        return self._get(url=self._build_url(endpoint))

    def create_gam_team(self, **request_body):
        endpoint = GAMEndpoint.TEAM.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_gam_team(self, team_id):
        endpoint = GAMEndpoint.TEAM_ID.value.format(id=team_id)
        return self._get(url=self._build_url(endpoint))

    def delete_gam_team(self, team_id):
        endpoint = GAMEndpoint.TEAM_ID.value.format(id=team_id)
        return self._delete(url=self._build_url(endpoint))

    def update_gam_team(self, team_id, **request_body):
        endpoint = GAMEndpoint.TEAM_ID.value.format(id=team_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_gam_user(self, user_id):
        endpoint = GAMEndpoint.USER_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))
