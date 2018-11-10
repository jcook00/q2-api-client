from client.endpoints.mobile_ws import LoginEndpoint
from client.services.base_client import Client
from client.utils.url import URL


class Q2Client(Client):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.base_path = kwargs.get('base_path')
        self.headers['Accept'] = "application/json"
        self.headers['q2token'] = kwargs.get('q2token') if kwargs.get('q2token') is not None else self.get_q2token()

    @property
    def base_path(self):
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        self._base_path = base_path

    def build_url(self, endpoint='/'):
        path = self._build_path(endpoint)
        url = URL(scheme=self.scheme, host=self.host, port=self.port, path=path)
        return url.build()

    def _build_path(self, endpoint):
        path = endpoint
        if self.base_path is not None:
            path = ''.join((self.base_path, path))
        return path

    def get_q2token(self):
        credentials = {'userId': self.username, 'password': self.password}
        endpoint = LoginEndpoint.LOGON_USER.value
        response = self.post(url=self.build_url(endpoint), json=credentials)
        response.raise_for_status()
        return response.headers.get('q2token')
