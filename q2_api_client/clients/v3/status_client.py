from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import StatusEndpoint


class StatusClient(BaseQ2Client):

    def get_action_status(self):
        """GET /v3/actionStatus

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = StatusEndpoint.ACTION_STATUS.value
        return self._get(url=self._build_url(endpoint))

    def get_rdc_status(self):
        """GET /v3/rdcStatus

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = StatusEndpoint.RDC_STATUS.value
        return self._get(url=self._build_url(endpoint))

    def get_recurring_action_status(self):
        """GET /v3/recurringActionStatus

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = StatusEndpoint.RECURRING_ACTION_STATUS.value
        return self._get(url=self._build_url(endpoint))
