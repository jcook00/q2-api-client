from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import EnumEndpoint


class EnumClient(BaseQ2Client):

    def get_currencies(self):
        """GET /v3/currency

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = EnumEndpoint.CURRENCY.value
        return self._get(url=self._build_url(endpoint))

    def get_products(self):
        """GET /v3/product

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = EnumEndpoint.PRODUCT.value
        return self._get(url=self._build_url(endpoint))
