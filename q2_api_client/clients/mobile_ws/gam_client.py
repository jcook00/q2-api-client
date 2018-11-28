from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import GAMEndpoint


class GAMClient(BaseQ2Client):

    def get_gam_lookup_tables(self):
        """GET /mobilews/gam/lookup

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.LOOKUP.value
        return self._get(url=self._build_url(endpoint))

    def get_gam_teams(self):
        """GET /mobilews/gam/team

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM.value
        return self._get(url=self._build_url(endpoint))

    def create_gam_team(self, request_body):
        """POST /mobilews/gam/team

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_gam_team(self, team_id):
        """GET /mobilews/gam/team/{id}

        :param str team_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM_ID.value.format(id=team_id)
        return self._get(url=self._build_url(endpoint))

    def delete_gam_team(self, team_id):
        """DELETE /mobilews/gam/team/{id}

        :param str team_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM_ID.value.format(id=team_id)
        return self._delete(url=self._build_url(endpoint))

    def update_gam_team(self, team_id, request_body):
        """PUT /mobilews/gam/team/{id}

        :param str team_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.TEAM_ID.value.format(id=team_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_gam_user(self, user_id):
        """GET /mobilews/gam/user/{id}

        :param str user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = GAMEndpoint.USER_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))
