from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AntiphishingEndpoint


class AntiphishingClient(BaseQ2Client):

    def get_antiphishing_phrase(self):
        """GET /mobilews/antiphishing

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AntiphishingEndpoint.ANTIPHISHING.value
        return self._get(url=self._build_url(endpoint))

    def create_antiphishing_phrase(self, request_body):
        """POST /mobilews/antiphishing

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AntiphishingEndpoint.ANTIPHISHING.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_antiphishing_phrase(self, request_body):
        """PUT /mobilews/antiphishing

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AntiphishingEndpoint.ANTIPHISHING.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_antiphishing_phrase_with_token(self, user_token):
        """GET /mobilews/antiphishing/{userToken}

        :param str user_token: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AntiphishingEndpoint.ANTIPHISHING_TOKEN.value.format(userToken=user_token)
        return self._get(url=self._build_url(endpoint))
