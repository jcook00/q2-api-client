from q2_api_client.clients.back_office.back_office_client import BackOfficeClient
from q2_api_client.clients.central.central_client import CentralClient
from q2_api_client.clients.file_map.file_map_client import FileMapClient
from q2_api_client.clients.hq.hq_client import HQClient
from q2_api_client.clients.mobile_ws.mobile_ws_client import MobileWSClient
from q2_api_client.clients.q2_config.q2_config_client import Q2ConfigClient
from q2_api_client.clients.refresh_cache.refresh_cache_client import RefreshCacheClient
from q2_api_client.clients.sdk.sdk_client import SDKClient
from q2_api_client.clients.v2.v2_client import V2Client
from q2_api_client.clients.v3.v3_client import V3Client


class Q2APIClient:

    def __init__(self, **kwargs):
        self._q2_config = Q2ConfigClient(**kwargs)
        kwargs['q2token'] = self._q2_config.get_header('q2token')
        self._central = CentralClient(**kwargs)
        self._file_map = FileMapClient(**kwargs)
        self._hq = HQClient(**kwargs)
        self._mobile_ws = MobileWSClient(**kwargs)
        self._refresh_cache = RefreshCacheClient(**kwargs)
        self._sdk = SDKClient(**kwargs)
        self._v2 = V2Client(**kwargs)
        self._v3 = V3Client(**kwargs)
        self._back_office_v3 = BackOfficeClient(**kwargs)

    @property
    def q2_config(self):
        return self._q2_config

    @property
    def central(self):
        return self._central

    @property
    def file_map(self):
        return self._file_map

    @property
    def hq(self):
        return self._hq

    @property
    def mobile_ws(self):
        return self._mobile_ws

    @property
    def refresh_cache(self):
        return self._refresh_cache

    @property
    def sdk(self):
        return self._sdk

    @property
    def v2(self):
        return self._v2

    @property
    def v3(self):
        return self._v3

    @property
    def back_office_v3(self):
        return self._back_office_v3

    def set_q2token(self, q2token):
        """Sets the Q2 Token for all the clients.

        :param q2token: the q2token value
        """
        def set_q2token(obj):
            put_header = getattr(obj, 'put_header', None)
            if callable(put_header):
                obj.put_header('q2token', q2token)
            else:
                for val in vars(obj).values():
                    set_q2token(val)

        for value in vars(self).values():
            set_q2token(value)
