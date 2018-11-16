from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import CalendarEndpoint


class CalendarClient(BaseQ2Client):

    def get_calendar(self):
        endpoint = CalendarEndpoint.CALENDAR.value
        return self._get(url=self._build_url(endpoint))

    def get_calendar_by_type(self, transaction_type):
        endpoint = CalendarEndpoint.CALENDAR_TRANSACTION_TYPE.value.format(transactionType=transaction_type)
        return self._get(url=self._build_url(endpoint))
