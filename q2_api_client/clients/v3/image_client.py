from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import ImageEndpoint


class ImageClient(BaseQ2Client):

    def retrieve_image(self, image_id):
        """POST /v3/image/{id}/retrieve

        :param str image_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ImageEndpoint.RETRIEVE_IMAGE.value.format(id=image_id)
        return self._post(url=self._build_url(endpoint))
