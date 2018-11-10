from client.endpoints.file_map import FileMapEndpoint
from client.services.q2_service import Q2Client


class FileMapService(Q2Client):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_file_map_asset(self, asset, **file_map):
        query_parameters = self.copy_query_parameters()
        query_parameters.update(**file_map)
        endpoint = FileMapEndpoint.FILE_MAP_ASSET.value.format(asset=asset)
        return self.get(url=self.build_url(endpoint), query_parameters=query_parameters)
