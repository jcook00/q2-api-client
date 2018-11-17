from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import RDCEndpoint


class RDCClient(BaseQ2Client):

    def get_rdc_history(self):
        """GET /mobilews/rdc

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RDC.value
        return self._get(url=self._build_url(endpoint))

    def delete_rdc(self):
        """DELETE /mobilews/rdc/new

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RDC_NEW.value
        return self._delete(url=self._build_url(endpoint))

    def get_rdc(self):
        """GET /mobilews/rdc/new

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RDC_NEW.value
        return self._get(url=self._build_url(endpoint))

    def create_rdc(self, request_body):
        """POST /mobilews/rdc/new

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RDC_NEW.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_rdc_detail(self, rdc_id):
        """GET /mobilews/rdc/{id}

        :param str rdc_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RDC_ID.value.format(id=rdc_id)
        return self._get(url=self._build_url(endpoint))

    def create_rdc_image(self, image_side):
        """POST /mobilews/rdc/{imageSide}

        :param str image_side: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RDCEndpoint.RDC_IMAGE.value.format(imageSide=image_side)
        return self._post(url=self._build_url(endpoint))
