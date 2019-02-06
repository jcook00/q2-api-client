from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import EnumEndpoint


class EnumClient(BaseQ2Client):

    def get_days_of_the_week(self):
        """GET /backoffice/v3/dayOfTheWeek

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = EnumEndpoint.DAY_OF_THE_WEEK.value
        return self._get(url=self._build_url(endpoint))
