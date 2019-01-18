from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import TypeEndpoint


class TypeClient(BaseQ2Client):

    def get_action_types(self):
        """GET /v3/actionType

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TypeEndpoint.ACTION_STATUS.value
        return self._get(url=self._build_url(endpoint))

    def get_image_types(self):
        """GET /v3/imageType

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TypeEndpoint.IMAGE_TYPE.value
        return self._get(url=self._build_url(endpoint))

    def get_product_types(self):
        """GET /v3/productType

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TypeEndpoint.PRODUCT_TYPE.value
        return self._get(url=self._build_url(endpoint))
