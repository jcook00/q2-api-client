from abc import ABCMeta
from collections import defaultdict
from copy import deepcopy

import requests


class RestClient(metaclass=ABCMeta):

    def __init__(self, **kwargs):
        self._connect_timeout = kwargs.get('connect_timeout')
        self._read_timeout = kwargs.get('read_timeout')
        self._host = kwargs.get('host')
        self._scheme = kwargs.get('scheme')
        self._port = kwargs.get('port')
        self._username = kwargs.get('username')
        self._password = kwargs.get('password')
        self._headers = kwargs.get('headers', dict())
        self._query_parameters = kwargs.get('query_parameters', defaultdict(set))
        self._fragment = kwargs.get('fragment')

    def get_header(self, header):
        return self._headers.get(header)

    def put_header(self, header, value):
        self._headers[header] = value

    def _copy_headers(self):
        return deepcopy(self._headers)

    def add_query_parameter(self, parameter, value):
        self._query_parameters[parameter].add(value)

    def _copy_query_parameters(self):
        return deepcopy(self._query_parameters)

    def _get(self, url, **components):
        r"""Sends a GET request.

        :param url: URL for the new :class:`Request` object.
        :param \*\*components: Optional arguments that ``request`` takes.
        :return: Response object
        :rtype: requests.Response
        """
        response = requests.get(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response

    def _put(self, url, **components):
        r"""Sends a PUT request.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*components: Optional arguments that ``request`` takes.
        :return: Response object
        :rtype: requests.Response
        """
        response = requests.put(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response

    def _post(self, url, **components):
        r"""Sends a POST request.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*components: Optional arguments that ``request`` takes.
        :return: Response object
        :rtype: requests.Response
        """
        response = requests.post(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response

    def _patch(self, url, **components):
        r"""Sends a PATCH request.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*components: Optional arguments that ``request`` takes.
        :return: Response object
        :rtype: requests.Response
        """
        response = requests.patch(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response

    def _delete(self, url, **components):
        r"""Sends a DELETE request.

        :param url: URL for the new :class:`Request` object.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) json data to send in the body of the :class:`Request`.
        :param \*\*components: Optional arguments that ``request`` takes.
        :return: Response object
        :rtype: requests.Response
        """
        response = requests.delete(
            url=url,
            params=components.get('query_parameters', self._query_parameters),
            headers=components.get('headers', self._headers),
            data=components.get('data'),
            json=components.get('json'),
            timeout=(self._connect_timeout, self._read_timeout)
        )
        return response
