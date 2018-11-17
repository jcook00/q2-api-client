from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AlertsEndpoint


class AlertsClient(BaseQ2Client):

    def get_alerts(self):
        endpoint = AlertsEndpoint.ALERTS.value
        return self._get(url=self._build_url(endpoint))

    def create_alert(self, **request_body):
        endpoint = AlertsEndpoint.ALERTS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_alert_form(self):
        endpoint = AlertsEndpoint.ALERTS_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_alert_form_by_type(self, form_type):
        endpoint = AlertsEndpoint.ALERTS_FORM_TYPE.value.format(type=form_type)
        return self._get(url=self._build_url(endpoint))

    def delete_alert(self, alert_id):
        endpoint = AlertsEndpoint.ALERTS_ID.value.format(id=alert_id)
        return self._delete(url=self._build_url(endpoint))

    def update_alert(self, alert_id, **request_body):
        endpoint = AlertsEndpoint.ALERTS_ID.value.format(id=alert_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_alert_by_type(self, alert_type):
        endpoint = AlertsEndpoint.ALERTS_TYPE.value.format(type=alert_type)
        return self._get(url=self._build_url(endpoint))
