from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import ReportEndpoint


class ReportClient(BaseQ2Client):

    def get_latest_report(self):
        endpoint = ReportEndpoint.REPORT_LATEST.value
        return self._get(url=self._build_url(endpoint))

    def get_report_plans(self):
        endpoint = ReportEndpoint.REPORT_PLAN.value
        return self._get(url=self._build_url(endpoint))

    def create_report_plan(self, **request_body):
        endpoint = ReportEndpoint.REPORT_PLAN.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_report_plan(self, plan_id):
        endpoint = ReportEndpoint.REPORT_PLAN_ID.value.format(id=plan_id)
        return self._get(url=self._build_url(endpoint))

    def delete_report_plan(self, plan_id):
        endpoint = ReportEndpoint.REPORT_PLAN_ID.value.format(id=plan_id)
        return self._delete(url=self._build_url(endpoint))

    def update_report_plan(self, plan_id, **request_body):
        endpoint = ReportEndpoint.REPORT_PLAN_ID.value.format(id=plan_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def execute_report_plan(self, plan_id):
        endpoint = ReportEndpoint.REPORT_PLAN_ID_RUN.value.format(id=plan_id)
        return self._get(url=self._build_url(endpoint))

    def get_reports_run(self):
        endpoint = ReportEndpoint.REPORT.value
        return self._get(url=self._build_url(endpoint))

    def get_report_output_list(self, report_id):
        endpoint = ReportEndpoint.REPORT_ID.value.format(id=report_id)
        return self._get(url=self._build_url(endpoint))

    def get_report_detail(self, report_id, detail_id):
        endpoint = ReportEndpoint.REPORT_DETAIL_ID.value.format(id=report_id, detailId=detail_id)
        return self._get(url=self._build_url(endpoint))

    def get_report_templates(self):
        endpoint = ReportEndpoint.REPORT_TEMPLATE.value
        return self._get(url=self._build_url(endpoint))

    def get_report_template(self, template_id):
        endpoint = ReportEndpoint.REPORT_TEMPLATE_ID.value.format(id=template_id)
        return self._get(url=self._build_url(endpoint))
