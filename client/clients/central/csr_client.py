from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.central_endpoints import CSREndpoint


class CSRClient(BaseQ2Client):

    def get_csr_config(self, name):
        """GET /central/csr/config/{name}

        :param str name: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.CONFIG.value.format(name=name)
        return self._get(url=self._build_url(endpoint))

    def get_csr_config_with_prefix(self, name, prefix):
        """GET /central/csr/config/{name}/{prefixNameWithLoginDot}

        :param str name: path parameter
        :param str prefix: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.CONFIG_PREFIXED.value.format(name=name, prefixNameWithLoginDot=prefix)
        return self._get(url=self._build_url(endpoint))

    def get_dashboard_activity(self):
        """GET /central/csr/dashboardActivity

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.DASHBOARD_ACTIVITY.value
        return self._get(url=self._build_url(endpoint))

    def get_csr_navigation(self):
        """GET /central/csr/nav

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.NAV.value
        return self._get(url=self._build_url(endpoint))

    def get_csr_properties(self):
        """GET /central/csr/properties

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CSREndpoint.PROPERTIES.value
        return self._get(url=self._build_url(endpoint))
