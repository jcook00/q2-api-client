from abc import ABCMeta
from collections import defaultdict
from copy import deepcopy

import requests


class Service(metaclass=ABCMeta):

    def __init__(self, **kwargs):
        self.host = kwargs.get('host')
        self.scheme = kwargs.get('scheme')
        self.port = kwargs.get('port')
        self.username = kwargs.get('username')
        self.password = kwargs.get('password')
        self.headers = kwargs.get('headers', dict())
        self.query_parameters = kwargs.get('query_parameters', defaultdict(set))
        self.fragment = kwargs.get('fragment')
        self.connect_timeout = kwargs.get('connect_timeout', 60)
        self.read_timeout = kwargs.get('read_timeout', 120)

    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        self._scheme = scheme

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        if not isinstance(host, str):
            raise ValueError("host must be a string")
        self._host = host

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if port is not None and not isinstance(port, int):
            raise ValueError("port must be an integer")
        self._port = port

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, headers):
        if isinstance(headers, dict):
            self._headers = headers

    def copy_headers(self):
        return deepcopy(self._headers)

    @property
    def query_parameters(self):
        return self._query_parameters

    @query_parameters.setter
    def query_parameters(self, query_parameters):
        if isinstance(query_parameters, defaultdict):
            self._query_parameters = query_parameters

    def copy_query_parameters(self):
        return deepcopy(self._query_parameters)

    @property
    def fragment(self):
        return self._fragment

    @fragment.setter
    def fragment(self, fragment):
        self._fragment = fragment

    def get(self, url, **components):
        response = requests.get(
            url=url,
            params=components.get('query_parameters', self.query_parameters),
            headers=components.get('headers', self.headers),
            timeout=(self.connect_timeout, self.read_timeout)
        )
        return response

    def put(self, url, **components):
        response = requests.put(
            url=url,
            params=components.get('query_parameters', self.query_parameters),
            headers=components.get('headers', self.headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self.connect_timeout, self.read_timeout)
        )
        return response

    def post(self, url, **components):
        response = requests.post(
            url=url,
            params=components.get('query_parameters', self.query_parameters),
            headers=components.get('headers', self.headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self.connect_timeout, self.read_timeout)
        )
        return response

    def patch(self, url, **components):
        response = requests.patch(
            url=url,
            params=components.get('query_parameters', self.query_parameters),
            headers=components.get('headers', self.headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self.connect_timeout, self.read_timeout)
        )
        return response

    def delete(self, url, **components):
        response = requests.delete(
            url=url,
            params=components.get('query_parameters', self.query_parameters),
            headers=components.get('headers', self.headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self.connect_timeout, self.read_timeout)
        )
        return response
