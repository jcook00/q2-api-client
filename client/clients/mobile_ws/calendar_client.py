from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import CalendarEndpoint


class CalendarClient(BaseQ2Client):

    def get_calendar(self):
        """GET /mobilews/calendar

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CalendarEndpoint.CALENDAR.value
        return self._get(url=self._build_url(endpoint))

    def get_calendar_by_type(self, transaction_type):
        """GET /mobilews/calendar/{transactionType}

        :param str transaction_type: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CalendarEndpoint.CALENDAR_TRANSACTION_TYPE.value.format(transactionType=transaction_type)
        return self._get(url=self._build_url(endpoint))
