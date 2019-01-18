from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import BranchEndpoint


class BranchClient(BaseQ2Client):

    def retrieve_branches(self):
        """POST /backoffice/v3/branch/retrieve

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BranchEndpoint.RETRIEVE_BRANCH.value
        return self._post(url=self._build_url(endpoint))
