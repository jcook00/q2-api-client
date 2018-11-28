from q2_api_client.clients.rest_client import RestClient
from q2_api_client.endpoints.mobile_ws_endpoints import LoginEndpoint
from q2_api_client.utils.url import URL


class BaseQ2Client(RestClient):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._connect_timeout = kwargs.get('connect_timeout', 60)
        self._read_timeout = kwargs.get('read_timeout', 120)
        self._scheme = kwargs.get('scheme', "https")
        self._base_path = kwargs.get('base_path')
        self._headers['Accept'] = "application/json"
        self._headers['q2token'] = kwargs.get('q2token') if kwargs.get('q2token') is not None else self._get_q2token()

    def _get_q2token(self):
        """Sends a logon POST request and returns the Q2 token from the response headers.

        :return: the q2token header value
        :rtype: str
        :raises HTTPError: failed to authenticate
        """
        request_body = {'userId': self._username, 'password': self._password}
        endpoint = LoginEndpoint.LOGON_USER.value
        response = self._post(url=self._build_url(endpoint), json=request_body)
        response.raise_for_status()
        return response.headers.get('q2token')

    def _build_url(self, endpoint='/'):
        """Builds a URL using the endpoint.

        :param str endpoint: the endpoint to add to the path
        :return: the URL
        :rtype: str
        """
        path = endpoint if self._base_path is None else "".join((self._base_path, endpoint))
        url = URL(scheme=self._scheme, host=self._host, port=self._port, path=path)
        return url.build()
