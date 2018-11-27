from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import CSREndpoint


class CSRClient(BaseQ2Client):

    def update_csr_config(self, request_body):
        """PUT /mobilews/csr/config

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.CONFIG.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_csr_config(self, name):
        """GET /mobilews/csr/config/{name}

        :param str name: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.CONFIG_NAME.value.format(name=name)
        return self._get(url=self._build_url(endpoint))

    def get_csr_config_with_prefix(self, name, prefix):
        """GET /mobilews/csr/config/{name}/{prefixNameWithLoginDot}

        :param str name: path parameter
        :param str prefix: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.CONFIG_NAME_PREFIXED.value.format(name=name, prefixNameWithLoginDot=prefix)
        return self._get(url=self._build_url(endpoint))

    def get_dashboard_activity(self):
        """GET /mobilews/csr/dashboardActivity

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.DASHBOARD_ACTIVITY.value
        return self._get(url=self._build_url(endpoint))

    def get_csr_navigation(self):
        """GET /mobilews/csr/nav

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.NAV.value
        return self._get(url=self._build_url(endpoint))

    def get_csr_properties(self):
        """GET /mobilews/csr/userProperties

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.PROPERTIES.value
        return self._get(url=self._build_url(endpoint))
