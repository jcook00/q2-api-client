from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import FeedsEndpoint


class FeedsClient(BaseQ2Client):

    def get_feeds(self, feed_type):
        """GET /mobilews/feeds/{type}

        :param str feed_type: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FeedsEndpoint.FEEDS.value.format(type=feed_type)
        return self._get(url=self._build_url(endpoint))

    def get_feed_checksum(self, feed_type, checksum):
        """GET /mobilews/feeds/{type}/{checksum}

        :param str feed_type: path parameter
        :param str checksum: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FeedsEndpoint.CHECKSUM.value.format(type=feed_type, checksum=checksum)
        return self._get(url=self._build_url(endpoint))
