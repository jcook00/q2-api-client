from client.clients.q2_client import Q2Client
from client.endpoints.hq import BackOfficeEndpoint


class BackOfficeClient(Q2Client):

    def get_addresses(self):
        endpoint = BackOfficeEndpoint.ADDRESS.value
        return self._get(url=self._build_url(endpoint))

    def get_address(self, address_id):
        endpoint = BackOfficeEndpoint.ADDRESS_ID.value.format(id=address_id)
        return self._get(url=self._build_url(endpoint))

    def create_address(self, **request_body):
        endpoint = BackOfficeEndpoint.ADDRESS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_address(self, address_id, **request_body):
        endpoint = BackOfficeEndpoint.ADDRESS_ID.value.format(id=address_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_address(self, address_id):
        endpoint = BackOfficeEndpoint.ADDRESS_ID.value.format(id=address_id)
        return self._delete(url=self._build_url(endpoint))

    def get_admin_users(self):
        endpoint = BackOfficeEndpoint.ADMIN_USER.value
        return self._get(url=self._build_url(endpoint))

    def get_admin_user(self, admin_user_id):
        endpoint = BackOfficeEndpoint.ADMIN_USER_ID.value.format(id=admin_user_id)
        return self._get(url=self._build_url(endpoint))

    def get_csr_notes(self):
        endpoint = BackOfficeEndpoint.CSR_NOTE.value
        return self._get(url=self._build_url(endpoint))

    def get_csr_note(self, csr_note_id):
        endpoint = BackOfficeEndpoint.CSR_NOTE_ID.value.format(id=csr_note_id)
        return self._get(url=self._build_url(endpoint))

    def create_csr_note(self, **request_body):
        endpoint = BackOfficeEndpoint.CSR_NOTE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_csr_note(self, csr_note_id):
        endpoint = BackOfficeEndpoint.CSR_NOTE_ID.value.format(id=csr_note_id)
        return self._delete(url=self._build_url(endpoint))

    def get_customers(self):
        endpoint = BackOfficeEndpoint.CUSTOMER.value
        return self._get(url=self._build_url(endpoint))

    def get_customer(self, customer_id):
        endpoint = BackOfficeEndpoint.CUSTOMER_ID.value.format(id=customer_id)
        return self._get(url=self._build_url(endpoint))

    def create_customer(self, **request_body):
        endpoint = BackOfficeEndpoint.CUSTOMER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_customer(self, customer_id, **request_body):
        endpoint = BackOfficeEndpoint.CUSTOMER_ID.value.format(id=customer_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_customer(self, customer_id):
        endpoint = BackOfficeEndpoint.CUSTOMER_ID.value.format(id=customer_id)
        return self._delete(url=self._build_url(endpoint))

    def get_subsidiaries(self, customer_id):
        endpoint = BackOfficeEndpoint.SUBSIDIARY.value.format(customerID=customer_id)
        return self._get(url=self._build_url(endpoint))

    def get_subsidiary(self, customer_id, subsidiary_id):
        endpoint = BackOfficeEndpoint.SUBSIDIARY_ID.value.format(customerID=customer_id, id=subsidiary_id)
        return self._get(url=self._build_url(endpoint))

    def create_subsidiary(self, customer_id, **request_body):
        endpoint = BackOfficeEndpoint.SUBSIDIARY.value.format(customerID=customer_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_subsidiary(self, customer_id, subsidiary_id, **request_body):
        endpoint = BackOfficeEndpoint.SUBSIDIARY_ID.value.format(customerID=customer_id, id=subsidiary_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_subsidiary(self, customer_id, subsidiary_id):
        endpoint = BackOfficeEndpoint.SUBSIDIARY_ID.value.format(customerID=customer_id, id=subsidiary_id)
        return self._delete(url=self._build_url(endpoint))

    def get_group_details(self):
        endpoint = BackOfficeEndpoint.GROUP_DETAIL.value
        return self._get(url=self._build_url(endpoint))

    def get_group_detail(self, group_id):
        endpoint = BackOfficeEndpoint.GROUP_DETAIL_ID.value.format(id=group_id)
        return self._get(url=self._build_url(endpoint))

    def get_host_accounts(self):
        endpoint = BackOfficeEndpoint.HOST_ACCOUNT.value
        return self._get(url=self._build_url(endpoint))

    def get_host_account(self, host_account_id):
        endpoint = BackOfficeEndpoint.HOST_ACCOUNT_ID.value.format(id=host_account_id)
        return self._get(url=self._build_url(endpoint))

    def get_service_charge_plans(self):
        endpoint = BackOfficeEndpoint.SERVICE_CHARGE_PLAN.value
        return self._get(url=self._build_url(endpoint))

    def get_service_charge_plan(self, plan_id):
        endpoint = BackOfficeEndpoint.SERVICE_CHARGE_PLAN_ID.value.format(id=plan_id)
        return self._get(url=self._build_url(endpoint))

    def get_system_properties(self):
        endpoint = BackOfficeEndpoint.SYSTEM_PROPERTY.value
        return self._get(url=self._build_url(endpoint))

    def get_system_property(self, property_id):
        endpoint = BackOfficeEndpoint.SYSTEM_PROPERTY_ID.value.format(id=property_id)
        return self._get(url=self._build_url(endpoint))

    def get_ui_config_properties_data(self):
        endpoint = BackOfficeEndpoint.CONFIG_PROPERTY_DATA.value
        return self._get(url=self._build_url(endpoint))

    def get_ui_config_property_data(self, property_id):
        endpoint = BackOfficeEndpoint.CONFIG_PROPERTY_DATA_ID.value.format(id=property_id)
        return self._get(url=self._build_url(endpoint))

    def get_users(self):
        endpoint = BackOfficeEndpoint.USER.value
        return self._get(url=self._build_url(endpoint))

    def get_user(self, user_id):
        endpoint = BackOfficeEndpoint.USER_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))

    def create_user(self, **request_body):
        endpoint = BackOfficeEndpoint.USER_ID.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_user(self, user_id, **request_body):
        endpoint = BackOfficeEndpoint.USER_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_user(self, user_id):
        endpoint = BackOfficeEndpoint.USER_ID.value.format(id=user_id)
        return self._delete(url=self._build_url(endpoint))

    def get_user_email(self, user_id):
        endpoint = BackOfficeEndpoint.USER_EMAIL.value.format(userID=user_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_phone(self, user_id):
        endpoint = BackOfficeEndpoint.USER_PHONE.value.format(userID=user_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_sac_targets(self, user_id):
        endpoint = BackOfficeEndpoint.USER_SAC_TARGETS.value.format(userID=user_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_logons(self):
        endpoint = BackOfficeEndpoint.USER_LOGON.value
        return self._get(url=self._build_url(endpoint))

    def get_user_logon(self, user_id):
        endpoint = BackOfficeEndpoint.USER_LOGON_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))

    def create_user_logon(self, **request_body):
        endpoint = BackOfficeEndpoint.USER_LOGON.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_user_logon(self, user_id, **request_body):
        endpoint = BackOfficeEndpoint.USER_LOGON_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_user_logon(self, user_id):
        endpoint = BackOfficeEndpoint.USER_LOGON_ID.value.format(id=user_id)
        return self._delete(url=self._build_url(endpoint))

    def get_user_logon_access_codes(self, user_logon_id):
        endpoint = BackOfficeEndpoint.USER_LOGON_ACCESS_CODES.value.format(userLogonID=user_logon_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_roles(self):
        endpoint = BackOfficeEndpoint.USER_ROLE.value
        return self._get(url=self._build_url(endpoint))

    def get_user_role(self, user_role_id):
        endpoint = BackOfficeEndpoint.USER_ROLE_ID.value.format(id=user_role_id)
        return self._get(url=self._build_url(endpoint))
