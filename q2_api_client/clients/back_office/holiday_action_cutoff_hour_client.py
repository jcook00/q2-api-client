from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import HolidayActionCutoffHourEndpoint


class HolidayActionCutoffHourClient(BaseQ2Client):

    def retrieve_holiday_action_cutoff_hours(self, request_body):
        """POST /backoffice/v3/holidayActionCutoffHour/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = HolidayActionCutoffHourEndpoint.RETRIEVE_HOLIDAY_ACTION_CUTOFFS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_holiday_action_cutoff_hours_by_id(self, cutoff_id):
        """POST /backoffice/v3/holidayActionCutoffHour/{id}/retrieve

        :param str cutoff_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = HolidayActionCutoffHourEndpoint.RETRIEVE_HOLIDAY_ACTION_CUTOFF.value.format(id=cutoff_id)
        return self._post(url=self._build_url(endpoint))
