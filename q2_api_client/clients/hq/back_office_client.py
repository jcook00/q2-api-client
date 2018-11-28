from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.hq_endpoints import BackOfficeEndpoint


class BackOfficeClient(BaseQ2Client):

    def get_addresses(self):
        """GET /hq/backOffice/address

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.ADDRESS.value
        return self._get(url=self._build_url(endpoint))

    def get_address(self, address_id):
        """GET /hq/backOffice/address/{id}

        :param int address_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.ADDRESS_ID.value.format(id=address_id)
        return self._get(url=self._build_url(endpoint))

    def create_address(self, request_body):
        """POST /hq/backOffice/address

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.ADDRESS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_address(self, address_id, request_body):
        """PUT /hq/backOffice/address/{id}

        :param int address_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.ADDRESS_ID.value.format(id=address_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_address(self, address_id):
        """DELETE /hq/backOffice/address/{id}

        :param int address_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.ADDRESS_ID.value.format(id=address_id)
        return self._delete(url=self._build_url(endpoint))

    def get_admin_users(self):
        """GET /hq/backOffice/adminUser

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.ADMIN_USER.value
        return self._get(url=self._build_url(endpoint))

    def get_admin_user(self, admin_user_id):
        """GET /hq/backOffice/adminUser/{id}

        :param int admin_user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.ADMIN_USER_ID.value.format(id=admin_user_id)
        return self._get(url=self._build_url(endpoint))

    def get_csr_notes(self):
        """GET /hq/backOffice/csrNote

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CSR_NOTE.value
        return self._get(url=self._build_url(endpoint))

    def get_csr_note(self, csr_note_id):
        """GET /hq/backOffice/csrNote/{id}

        :param int csr_note_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CSR_NOTE_ID.value.format(id=csr_note_id)
        return self._get(url=self._build_url(endpoint))

    def create_csr_note(self, request_body):
        """POST /hq/backOffice/csrNote

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CSR_NOTE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_csr_note(self, csr_note_id):
        """DELETE /hq/backOffice/csrNote/{id}

        :param int csr_note_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CSR_NOTE_ID.value.format(id=csr_note_id)
        return self._delete(url=self._build_url(endpoint))

    def get_customers(self):
        """GET /hq/backOffice/customer

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CUSTOMER.value
        return self._get(url=self._build_url(endpoint))

    def get_customer(self, customer_id):
        """GET /hq/backOffice/customer/{id}

        :param int customer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CUSTOMER_ID.value.format(id=customer_id)
        return self._get(url=self._build_url(endpoint))

    def create_customer(self, request_body):
        """POST /hq/backOffice/customer

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CUSTOMER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_customer(self, customer_id, request_body):
        """PUT /hq/backOffice/customer/{id}

        :param int customer_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CUSTOMER_ID.value.format(id=customer_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_customer(self, customer_id):
        """DELETE /hq/backOffice/customer/{id}

        :param int customer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CUSTOMER_ID.value.format(id=customer_id)
        return self._delete(url=self._build_url(endpoint))

    def get_subsidiaries(self, customer_id):
        """GET /hq/backOffice/customer/{customerID}/subsidiary

        :param int customer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SUBSIDIARY.value.format(customerID=customer_id)
        return self._get(url=self._build_url(endpoint))

    def get_subsidiary(self, customer_id, subsidiary_id):
        """GET /hq/backOffice/customer/{customerID}/subsidiary/{id}

        :param int customer_id: path parameter
        :param int subsidiary_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SUBSIDIARY_ID.value.format(customerID=customer_id, id=subsidiary_id)
        return self._get(url=self._build_url(endpoint))

    def create_subsidiary(self, customer_id, request_body):
        """POST /hq/backOffice/customer/{customerID}/subsidiary

        :param int customer_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SUBSIDIARY.value.format(customerID=customer_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_subsidiary(self, customer_id, subsidiary_id, request_body):
        """PUT /hq/backOffice/customer/{customerID}/subsidiary/{id}

        :param int customer_id: path parameter
        :param int subsidiary_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SUBSIDIARY_ID.value.format(customerID=customer_id, id=subsidiary_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_subsidiary(self, customer_id, subsidiary_id):
        """DELETE /hq/backOffice/customer/{customerID}/subsidiary/{id}

        :param int customer_id: path parameter
        :param int subsidiary_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SUBSIDIARY_ID.value.format(customerID=customer_id, id=subsidiary_id)
        return self._delete(url=self._build_url(endpoint))

    def get_group_details(self):
        """GET /hq/backOffice/groupDetail

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.GROUP_DETAIL.value
        return self._get(url=self._build_url(endpoint))

    def get_group_detail(self, group_id):
        """GET /hq/backOffice/groupDetail/{id}

        :param int group_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.GROUP_DETAIL_ID.value.format(id=group_id)
        return self._get(url=self._build_url(endpoint))

    def get_host_accounts(self):
        """GET /hq/backOffice/hostAccount

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.HOST_ACCOUNT.value
        return self._get(url=self._build_url(endpoint))

    def get_host_account(self, host_account_id):
        """GET /hq/backOffice/hostAccount/{id}

        :param int host_account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.HOST_ACCOUNT_ID.value.format(id=host_account_id)
        return self._get(url=self._build_url(endpoint))

    def get_service_charge_plans(self):
        """GET /hq/backOffice/serviceChargePlan

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SERVICE_CHARGE_PLAN.value
        return self._get(url=self._build_url(endpoint))

    def get_service_charge_plan(self, plan_id):
        """GET /hq/backOffice/serviceChargePlan/{id}

        :param int plan_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SERVICE_CHARGE_PLAN_ID.value.format(id=plan_id)
        return self._get(url=self._build_url(endpoint))

    def get_system_properties(self):
        """GET /hq/backOffice/systemProperty

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SYSTEM_PROPERTY.value
        return self._get(url=self._build_url(endpoint))

    def get_system_property(self, property_id):
        """GET /hq/backOffice/systemProperty/{id}

        :param int property_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.SYSTEM_PROPERTY_ID.value.format(id=property_id)
        return self._get(url=self._build_url(endpoint))

    def get_ui_config_properties_data(self):
        """GET /hq/backOffice/uIConfigPropertyData

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CONFIG_PROPERTY_DATA.value
        return self._get(url=self._build_url(endpoint))

    def get_ui_config_property_data(self, property_id):
        """GET /hq/backOffice/uIConfigPropertyData/{id}

        :param int property_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.CONFIG_PROPERTY_DATA_ID.value.format(id=property_id)
        return self._get(url=self._build_url(endpoint))

    def get_users(self):
        """GET /hq/backOffice/user

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER.value
        return self._get(url=self._build_url(endpoint))

    def get_user(self, user_id):
        """GET /hq/backOffice/user/{id}

        :param int user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))

    def create_user(self, request_body):
        """POST /hq/backOffice/user

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_user(self, user_id, request_body):
        """PUT /hq/backOffice/user/{id}

        :param int user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_user(self, user_id):
        """DELETE /hq/backOffice/user/{id}

        :param int user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_ID.value.format(id=user_id)
        return self._delete(url=self._build_url(endpoint))

    def get_user_email(self, user_id):
        """GET /hq/backOffice/user/{userID}/email

        :param int user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_EMAIL.value.format(userID=user_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_phone(self, user_id):
        """GET /hq/backOffice/user/{userID}/phone

        :param int user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_PHONE.value.format(userID=user_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_sac_targets(self, user_id):
        """GET /hq/backOffice/user/{userID}/sacTargets

        :param int user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_SAC_TARGETS.value.format(userID=user_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_logons(self):
        """GET /hq/backOffice/userLogon

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_LOGON.value
        return self._get(url=self._build_url(endpoint))

    def get_user_logon(self, user_id):
        """GET /hq/backOffice/userLogon/{id}

        :param int user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_LOGON_ID.value.format(id=user_id)
        return self._get(url=self._build_url(endpoint))

    def create_user_logon(self, request_body):
        """POST /hq/backOffice/userLogon

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_LOGON.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_user_logon(self, user_id, request_body):
        """PUT /hq/backOffice/userLogon/{id}

        :param int user_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_LOGON_ID.value.format(id=user_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_user_logon(self, user_id):
        """DELETE /hq/backOffice/userLogon/{id}

        :param int user_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_LOGON_ID.value.format(id=user_id)
        return self._delete(url=self._build_url(endpoint))

    def get_user_logon_access_codes(self, user_logon_id):
        """GET /hq/backOffice/userLogon/{userLogonID}/accessCodes

        :param int user_logon_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_LOGON_ACCESS_CODES.value.format(userLogonID=user_logon_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_roles(self):
        """GET /hq/backOffice/userRole

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_ROLE.value
        return self._get(url=self._build_url(endpoint))

    def get_user_role(self, user_role_id):
        """GET /hq/backOffice/userRole/{id}

        :param int user_role_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BackOfficeEndpoint.USER_ROLE_ID.value.format(id=user_role_id)
        return self._get(url=self._build_url(endpoint))
