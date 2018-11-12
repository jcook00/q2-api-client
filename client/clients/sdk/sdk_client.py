from client.clients.q2_client import Q2Client
from client.endpoints.sdk import SDKEndpoint


class SDKClient(Q2Client):

    def get_passthrough_route(self, endpoint):
        sdk_endpoint = SDKEndpoint.ENDPOINT.value.format(endpoint=endpoint)
        return self._get(url=self._build_url(sdk_endpoint))

    def delete_passthrough_route(self, endpoint):
        sdk_endpoint = SDKEndpoint.ENDPOINT.value.format(endpoint=endpoint)
        return self._delete(url=self._build_url(sdk_endpoint))

    def create_passthrough_route(self, endpoint):
        sdk_endpoint = SDKEndpoint.ENDPOINT.value.format(endpoint=endpoint)
        return self._post(url=self._build_url(sdk_endpoint))

    def update_passthrough_route(self, endpoint):
        sdk_endpoint = SDKEndpoint.ENDPOINT.value.format(endpoint=endpoint)
        return self._put(url=self._build_url(sdk_endpoint))

    def get_passthrough_route_with_path(self, endpoint, path):
        sdk_endpoint = SDKEndpoint.ENDPOINT_PATH.value.format(endpoint=endpoint, path=path)
        return self._get(url=self._build_url(sdk_endpoint))

    def delete_passthrough_route_with_path(self, endpoint, path):
        sdk_endpoint = SDKEndpoint.ENDPOINT_PATH.value.format(endpoint=endpoint, path=path)
        return self._delete(url=self._build_url(sdk_endpoint))

    def create_passthrough_route_with_path(self, endpoint, path):
        sdk_endpoint = SDKEndpoint.ENDPOINT_PATH.value.format(endpoint=endpoint, path=path)
        return self._post(url=self._build_url(sdk_endpoint))

    def update_passthrough_route_with_path(self, endpoint, path):
        sdk_endpoint = SDKEndpoint.ENDPOINT_PATH.value.format(endpoint=endpoint, path=path)
        return self._put(url=self._build_url(sdk_endpoint))
