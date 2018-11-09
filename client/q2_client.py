from client.services.file_map_service import FileMapService
from client.services.q2_config_service import Q2ConfigService


class Q2Client(object):

    def __init__(self, **kwargs):
        self.q2_config = Q2ConfigService(**kwargs)
        kwargs['q2token'] = self.q2_config.headers.get('q2token')
        self.file_map = FileMapService(**kwargs)
