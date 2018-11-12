from client.clients.q2_client import Q2Client
from client.endpoints.central_endpoints import GAMEndpoint


class GAMClient(Q2Client):

    def get_gam_rights(self):
        endpoint = GAMEndpoint.RIGHTS.value
        return self._get(url=self._build_url(endpoint))

    def get_gam_teams(self):
        endpoint = GAMEndpoint.TEAM.value
        return self._get(url=self._build_url(endpoint))

    def create_gam_team(self, **request_body):
        endpoint = GAMEndpoint.TEAM.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_gam_team(self, team_id):
        endpoint = GAMEndpoint.TEAM_ID.value.format(team_id=team_id)
        return self._get(url=self._build_url(endpoint))

    def delete_gam_team(self, team_id):
        endpoint = GAMEndpoint.TEAM_ID.value.format(team_id=team_id)
        return self._delete(url=self._build_url(endpoint))

    def get_gam_user(self, user_id):
        endpoint = GAMEndpoint.USER_ID.value.format(user_id=user_id)
        return self._get(url=self._build_url(endpoint))
