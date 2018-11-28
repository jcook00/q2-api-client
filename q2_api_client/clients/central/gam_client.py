from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.central_endpoints import GAMEndpoint


class GAMClient(BaseQ2Client):

    def get_gam_rights(self):
        """GET /central/gam/rights

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.RIGHTS.value
        return self._get(url=self._build_url(endpoint))

    def get_gam_teams(self):
        """GET /central/gam/team

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM.value
        return self._get(url=self._build_url(endpoint))

    def create_gam_team(self, request_body):
        """POST /central/gam/team

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_gam_team(self, team_id):
        """GET /central/gam/team/{team_id}

        :param int team_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM_ID.value.format(team_id=team_id)
        return self._get(url=self._build_url(endpoint))

    def delete_gam_team(self, team_id):
        """DELETE /central/gam/team/{team_id}

        :param int team_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM_ID.value.format(team_id=team_id)
        return self._delete(url=self._build_url(endpoint))

    def get_gam_user(self, user_id):
        """GET /central/gam/user/{user_id}

        :param int user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.USER_ID.value.format(user_id=user_id)
        return self._get(url=self._build_url(endpoint))
