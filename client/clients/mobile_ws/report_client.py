from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import ReportEndpoint


class ReportClient(BaseQ2Client):

    def get_latest_report(self):
        """GET /mobilews/report/latest

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_LATEST.value
        return self._get(url=self._build_url(endpoint))

    def get_report_plans(self):
        """GET /mobilews/report/plan

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_PLAN.value
        return self._get(url=self._build_url(endpoint))

    def create_report_plan(self, request_body):
        """POST /mobilews/report/plan

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_PLAN.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_report_plan(self, plan_id):
        """GET /mobilews/report/plan/{id}

        :param str plan_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_PLAN_ID.value.format(id=plan_id)
        return self._get(url=self._build_url(endpoint))

    def delete_report_plan(self, plan_id):
        """DELETE /mobilews/report/plan/{id}

        :param str plan_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_PLAN_ID.value.format(id=plan_id)
        return self._delete(url=self._build_url(endpoint))

    def update_report_plan(self, plan_id, request_body):
        """PUT /mobilews/report/plan/{id}

        :param str plan_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_PLAN_ID.value.format(id=plan_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def execute_report_plan(self, plan_id):
        """GET /mobilews/report/plan/{id}/run

        :param str plan_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_PLAN_ID_RUN.value.format(id=plan_id)
        return self._get(url=self._build_url(endpoint))

    def get_reports_run(self):
        """GET /mobilews/report/report

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT.value
        return self._get(url=self._build_url(endpoint))

    def get_report_output_list(self, report_id):
        """GET /mobilews/report/report/{id}

        :param str report_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_ID.value.format(id=report_id)
        return self._get(url=self._build_url(endpoint))

    def get_report_detail(self, report_id, detail_id):
        """GET /mobilews/report/report/{id}/{detailId}

        :param str report_id: path parameter
        :param str detail_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_DETAIL_ID.value.format(id=report_id, detailId=detail_id)
        return self._get(url=self._build_url(endpoint))

    def get_report_templates(self):
        """GET /mobilews/report/template

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_TEMPLATE.value
        return self._get(url=self._build_url(endpoint))

    def get_report_template(self, template_id):
        """GET /mobilews/report/template/{id}

        :param str template_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ReportEndpoint.REPORT_TEMPLATE_ID.value.format(id=template_id)
        return self._get(url=self._build_url(endpoint))
