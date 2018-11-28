from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import AlertsEndpoint


class AlertsClient(BaseQ2Client):

    def get_alerts(self):
        """GET /mobilews/alerts

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AlertsEndpoint.ALERTS.value
        return self._get(url=self._build_url(endpoint))

    def create_alert(self, request_body):
        """POST /mobilews/alerts

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AlertsEndpoint.ALERTS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_alert_form(self):
        """GET /mobilews/alerts/form

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AlertsEndpoint.ALERTS_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_alert_form_by_type(self, form_type):
        """GET /mobilews/alerts/form/{type}

        :param str form_type: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AlertsEndpoint.ALERTS_FORM_TYPE.value.format(type=form_type)
        return self._get(url=self._build_url(endpoint))

    def delete_alert(self, alert_id):
        """DELETE /mobilews/alerts/{id}

        :param str alert_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AlertsEndpoint.ALERTS_ID.value.format(id=alert_id)
        return self._delete(url=self._build_url(endpoint))

    def update_alert(self, alert_id, request_body):
        """PUT /mobilews/alerts/{id}

        :param str alert_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AlertsEndpoint.ALERTS_ID.value.format(id=alert_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_alert_by_type(self, alert_type):
        """GET /mobilews/alerts/{type}

        :param str alert_type: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AlertsEndpoint.ALERTS_TYPE.value.format(type=alert_type)
        return self._get(url=self._build_url(endpoint))
