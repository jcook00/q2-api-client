from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.sdk_endpoints import SDKEndpoint


class SDKClient(BaseQ2Client):

    def get_passthrough_route(self, endpoint):
        """GET /sdk/{endpoint}

        :param str endpoint: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        sdk_endpoint = SDKEndpoint.ENDPOINT.value.format(endpoint=endpoint)
        return self._get(url=self._build_url(sdk_endpoint))

    def delete_passthrough_route(self, endpoint):
        """DELETE /sdk/{endpoint}

        :param str endpoint: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        sdk_endpoint = SDKEndpoint.ENDPOINT.value.format(endpoint=endpoint)
        return self._delete(url=self._build_url(sdk_endpoint))

    def create_passthrough_route(self, endpoint):
        """POST /sdk/{endpoint}

        :param str endpoint: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        sdk_endpoint = SDKEndpoint.ENDPOINT.value.format(endpoint=endpoint)
        return self._post(url=self._build_url(sdk_endpoint))

    def update_passthrough_route(self, endpoint):
        """PUT /sdk/{endpoint}

        :param str endpoint: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        sdk_endpoint = SDKEndpoint.ENDPOINT.value.format(endpoint=endpoint)
        return self._put(url=self._build_url(sdk_endpoint))

    def get_passthrough_route_with_path(self, endpoint, path):
        """GET /sdk/{endpoint}/{path}

        :param str endpoint: path parameter
        :param str path: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        sdk_endpoint = SDKEndpoint.ENDPOINT_PATH.value.format(endpoint=endpoint, path=path)
        return self._get(url=self._build_url(sdk_endpoint))

    def delete_passthrough_route_with_path(self, endpoint, path):
        """DELETE /sdk/{endpoint}/{path}

        :param str endpoint: path parameter
        :param str path: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        sdk_endpoint = SDKEndpoint.ENDPOINT_PATH.value.format(endpoint=endpoint, path=path)
        return self._delete(url=self._build_url(sdk_endpoint))

    def create_passthrough_route_with_path(self, endpoint, path):
        """POST /sdk/{endpoint}/{path}

        :param str endpoint: path parameter
        :param str path: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        sdk_endpoint = SDKEndpoint.ENDPOINT_PATH.value.format(endpoint=endpoint, path=path)
        return self._post(url=self._build_url(sdk_endpoint))

    def update_passthrough_route_with_path(self, endpoint, path):
        """PUT /sdk/{endpoint}/{path}

        :param str endpoint: path parameter
        :param str path: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        sdk_endpoint = SDKEndpoint.ENDPOINT_PATH.value.format(endpoint=endpoint, path=path)
        return self._put(url=self._build_url(sdk_endpoint))
