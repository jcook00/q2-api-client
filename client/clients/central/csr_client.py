from client.clients.q2_client import Q2Client
from client.endpoints.central import CSREndpoint


class CSRClient(Q2Client):

    def get_csr_config(self, name):
        endpoint = CSREndpoint.CONFIG.value.format(name=name)
        return self.get(url=self.build_url(endpoint))

    def get_csr_config_with_prefix(self, name, prefix):
        endpoint = CSREndpoint.CONFIG_PREFIXED.value.format(name=name, prefixNameWithLoginDot=prefix)
        return self.get(url=self.build_url(endpoint))

    def get_dashboard_activity(self):
        endpoint = CSREndpoint.DASHBOARD_ACTIVITY.value
        return self.get(url=self.build_url(endpoint))

    def get_csr_navigation(self):
        endpoint = CSREndpoint.NAV.value
        return self.get(url=self.build_url(endpoint))

    def get_csr_properties(self):
        endpoint = CSREndpoint.PROPERTIES.value
        return self.get(url=self.build_url(endpoint))