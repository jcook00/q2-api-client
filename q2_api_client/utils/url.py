from collections import defaultdict
from urllib import parse
from urllib.parse import urlencode, urlunparse


class URL:

    BASE_PATH = "/"

    def __init__(self, **components):
        self._scheme = None
        self._host = None
        self._port = None
        self._path = None
        self._params = None
        self._query = None
        self._fragment = None
        self._username = None
        self._password = None
        self._set_url_components(**components)

    def _set_url_components(self, **components):
        self.scheme = components.get('scheme')
        self.host = components.get('host')
        self.port = components.get('port')
        self.path = components.get('path', self.BASE_PATH)
        self.params = components.get('params', defaultdict(set))
        self.query = components.get('query', defaultdict(set))
        self.fragment = components.get('fragment')
        self.username = components.get('username')
        self.password = components.get('password')

    @property
    def scheme(self):
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        if scheme not in parse.uses_netloc:
            exception_msg = "scheme must be one of the following: {}".format(parse.uses_netloc)
            raise ValueError(exception_msg)
        self._scheme = scheme

    @property
    def host(self):
        return self._host

    @host.setter
    def host(self, host):
        self._host = host

    @property
    def netloc(self):
        netloc = self.host
        if self.username is not None and self.password is not None:
            auth = ":".join((self.username, self.password))
            netloc = "@".join((auth, netloc))
        if self.port is not None:
            netloc = ":".join((netloc, str(self.port)))
        return netloc

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if port is not None and int(port) <= 0:
            raise ValueError("port must be a positive integer")
        self._port = port

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        if path is None:
            self._path = self.BASE_PATH
        elif not path.startswith(self.BASE_PATH):
            self._path = "".join((self.BASE_PATH, path))
        else:
            self._path = path

    @property
    def fragment(self):
        return self._fragment

    @fragment.setter
    def fragment(self, fragment):
        self._fragment = fragment

    @property
    def params(self):
        return self._params

    @params.setter
    def params(self, params):
        self._params = params

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, query):
        self._query = query

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

    @staticmethod
    def _urlencode(query, doseq=True):
        return urlencode(query=query, doseq=doseq, encoding='utf-8')

    def build(self, doseq=True):
        return urlunparse(
            (self.scheme,
             self.netloc,
             self.path,
             self._urlencode(query=self.params, doseq=doseq),
             self._urlencode(query=self.query, doseq=doseq),
             self.fragment)
        )
