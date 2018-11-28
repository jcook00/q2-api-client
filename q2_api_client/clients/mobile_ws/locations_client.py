from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import LocationsEndpoint


class LocationsClient(BaseQ2Client):

    def get_locations(self):
        """GET /mobilews/locations

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LocationsEndpoint.LOCATIONS.value
        return self._get(url=self._build_url(endpoint))

    def get_location_address(self, address):
        """GET /mobilews/locations/address/{address}

        :param str address: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LocationsEndpoint.ADDRESS.value.format(address=address)
        return self._get(url=self._build_url(endpoint))

    def get_location_address_coordinates(self, address, latitude, longitude):
        """GET /mobilews/locations/address/{address}/{latitude}/{longitude}

        :param str address: path parameter
        :param str latitude: path parameter
        :param str longitude: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LocationsEndpoint.ADDRESS_COORDINATES.value.format(address=address, latitude=latitude, longitude=longitude)
        return self._get(url=self._build_url(endpoint))

    def get_locations_coordinates(self, latitude, longitude):
        """GET /mobilews/locations/{latitude}/{longitude}

        :param str latitude: path parameter
        :param str longitude: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LocationsEndpoint.LOCATIONS_COORDINATES.value.format(latitude=latitude, longitude=longitude)
        return self._get(url=self._build_url(endpoint))
