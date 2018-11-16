from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import LocationsEndpoint


class LocationsClient(BaseQ2Client):

    def get_locations(self):
        endpoint = LocationsEndpoint.LOCATIONS.value
        return self._get(url=self._build_url(endpoint))

    def get_location_address(self, address):
        endpoint = LocationsEndpoint.ADDRESS.value.format(address=address)
        return self._get(url=self._build_url(endpoint))

    def get_location_address_coordinates(self, address, latitude, longitude):
        endpoint = LocationsEndpoint.ADDRESS_LAT_LONG.value.format(address=address, latitude=latitude, longitude=longitude)
        return self._get(url=self._build_url(endpoint))

    def get_locations_coordinates(self, latitude, longitude):
        endpoint = LocationsEndpoint.LOCATIONS_LAT_LONG.value.format(latitude=latitude, longitude=longitude)
        return self._get(url=self._build_url(endpoint))
