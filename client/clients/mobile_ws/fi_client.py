from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import FIEndpoint


class FIClient(BaseQ2Client):

    def get_fi_list(self):
        """GET /mobilews/fi

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FIEndpoint.FI.value
        return self._get(url=self._build_url(endpoint))

    def get_fi(self, wedge_lookup_id):
        """GET /mobilews/fi/{wedgeLookupId}

        :param str wedge_lookup_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FIEndpoint.FI_WEDGE_LOOKUP.value.format(wedgeLookupId=wedge_lookup_id)
        return self._get(url=self._build_url(endpoint))
