from client.clients.q2_client import Q2Client
from client.endpoints.file_map import FileMapEndpoint


class FileMapClient(Q2Client):

    def get_file_map_asset(self, asset, **query):
        endpoint = FileMapEndpoint.FILE_MAP_ASSET.value.format(asset=asset)
        query_parameters = self.copy_query_parameters()
        query_parameters.update(**query)
        return self.get(url=self.build_url(endpoint), query_parameters=query_parameters)
