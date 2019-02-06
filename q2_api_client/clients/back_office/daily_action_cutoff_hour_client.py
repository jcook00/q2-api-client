from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import DailyActionCutoffHourEndpoint


class DailyActionCutoffHourClient(BaseQ2Client):

    def retrieve_daily_action_cutoff_hours(self, request_body):
        """POST /backoffice/v3/dailyActionCutoffHour/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = DailyActionCutoffHourEndpoint.RETRIEVE_DAILY_ACTION_CUTOFFS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_daily_action_cutoff_hours_by_id(self, cutoff_id):
        """POST /backoffice/v3/dailyActionCutoffHour/{id}/retrieve

        :param str cutoff_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = DailyActionCutoffHourEndpoint.RETRIEVE_DAILY_ACTION_CUTOFF.value.format(id=cutoff_id)
        return self._post(url=self._build_url(endpoint))

    def update_daily_action_cutoff_hours(self, cutoff_id, request_body):
        """POST /backoffice/v3/dailyActionCutoffHour/{id}/update

        :param str cutoff_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = DailyActionCutoffHourEndpoint.UPDATE_DAILY_ACTION_CUTOFFS.value.format(id=cutoff_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
