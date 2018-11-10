from abc import ABCMeta
from collections import defaultdict
from copy import deepcopy

import requests


class RestClient(metaclass=ABCMeta):

    def __init__(self, **kwargs):
        self._host = kwargs.get('host')
        self._scheme = kwargs.get('scheme')
        self._port = kwargs.get('port')
        self._username = kwargs.get('username')
        self._password = kwargs.get('password')
        self._headers = kwargs.get('headers', dict())
        self._query_parameters = kwargs.get('query_parameters', defaultdict(set))
        self._fragment = kwargs.get('fragment')
        self._connect_timeout = kwargs.get('connect_timeout', 60)
        self._read_timeout = kwargs.get('read_timeout', 120)

    @property
    def scheme(self):
        return self._scheme

    @property
    def host(self):
        return self._host

    @property
    def port(self):
        return self._port

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password

    @property
    def headers(self):
        return self._headers

    def copy_headers(self):
        return deepcopy(self._headers)

    @property
    def query_parameters(self):
        return self._query_parameters

    def copy_query_parameters(self):
        return deepcopy(self._query_parameters)

    @property
    def fragment(self):
        return self._fragment

    @property
    def connect_timeout(self):
        return self._connect_timeout

    @property
    def read_timeout(self):
        return self._read_timeout

    def get(self, url, **components):
        response = requests.get(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response

    def put(self, url, **components):
        response = requests.put(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response

    def post(self, url, **components):
        response = requests.post(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response

    def patch(self, url, **components):
        response = requests.patch(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response

    def delete(self, url, **components):
        response = requests.delete(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response
