from client.clients.q2_client import Q2Client
from client.endpoints.v2 import PFMEndpoint


class PFMClient(Q2Client):

    def get_account(self, account_guid, **query):
        endpoint = PFMEndpoint.ACCOUNT_GUID.value.format(accountGuid=account_guid)
        query_parameters = self._copy_query_parameters()
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def update_account(self, account_guid, **request_body):
        endpoint = PFMEndpoint.ACCOUNT_GUID.value.format(accountGuid=account_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_categories(self):
        endpoint = PFMEndpoint.CATEGORIES.value
        return self._get(url=self._build_url(endpoint))

    def create_category(self, **request_body):
        endpoint = PFMEndpoint.CATEGORIES.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_category(self, category_guid):
        endpoint = PFMEndpoint.CATEGORY_GUID.value.format(categoryGuid=category_guid)
        return self._delete(url=self._build_url(endpoint))

    def update_category(self, category_guid, **request_body):
        endpoint = PFMEndpoint.CATEGORY_GUID.value.format(categoryGuid=category_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_institutions(self, **query):
        endpoint = PFMEndpoint.INSTITUTIONS.value
        query_parameters = self._copy_query_parameters()
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def get_institution(self, institution_guid):
        endpoint = PFMEndpoint.INSTITUTION_GUID.value.format(institutionGuid=institution_guid)
        return self._get(url=self._build_url(endpoint))

    def get_institution_credentials(self, institution_guid):
        endpoint = PFMEndpoint.INSTITUTION_CREDENTIALS.value.format(institutionGuid=institution_guid)
        return self._get(url=self._build_url(endpoint))

    def get_job(self, job_guid):
        endpoint = PFMEndpoint.JOB.value.format(jobGuid=job_guid)
        return self._get(url=self._build_url(endpoint))

    def get_job_mfa_credentials(self, job_guid):
        endpoint = PFMEndpoint.JOB_MFA_CREDENTIALS.value.format(jobGuid=job_guid)
        return self._get(url=self._build_url(endpoint))

    def resume_job(self, job_guid):
        endpoint = PFMEndpoint.JOB_RESUME.value.format(jobGuid=job_guid)
        return self._post(url=self._build_url(endpoint))

    def get_member(self, member_guid):
        endpoint = PFMEndpoint.MEMBER_GUID.value.format(memberGuid=member_guid)
        return self._get(url=self._build_url(endpoint))

    def create_member(self, **request_body):
        endpoint = PFMEndpoint.MEMBERS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_member(self, member_guid, **request_body):
        endpoint = PFMEndpoint.MEMBER_GUID.value.format(memberGuid=member_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_member(self, member_guid):
        endpoint = PFMEndpoint.MEMBER_GUID.value.format(memberGuid=member_guid)
        return self._delete(url=self._build_url(endpoint))

    def delete_all_members(self):
        endpoint = PFMEndpoint.ALL_MEMBERS.value
        return self._delete(url=self._build_url(endpoint))

    def create_member_credentials(self, member_guid, **request_body):
        endpoint = PFMEndpoint.MEMBER_CREDENTIALS.value.format(memberGuid=member_guid)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def refresh_member(self, member_guid):
        endpoint = PFMEndpoint.MEMBER_REFRESH.value.format(memberGuid=member_guid)
        return self._post(url=self._build_url(endpoint))

    def update_transaction(self, transaction_guid, **request_body):
        endpoint = PFMEndpoint.TRANSACTION_GUID.value.format(transactionGuid=transaction_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def update_split_transaction(self, transaction_guid, **request_body):
        endpoint = PFMEndpoint.TRANSACTION_SPLITS.value.format(transactionGuid=transaction_guid)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def create_mx_user(self):
        endpoint = PFMEndpoint.USERS.value
        return self._post(url=self._build_url(endpoint))

    def get_widget(self, widget_short_name, **query):
        endpoint = PFMEndpoint.WIDGET.value.format(widgetShortName=widget_short_name)
        query_parameters = self._copy_query_parameters()
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)
