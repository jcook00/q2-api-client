from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import CommercialEndpoint


class CommercialClient(BaseQ2Client):

    def reprocess_ach_import(self, request_body):
        """PUT /mobilews/commercial/achImport

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.ACH_IMPORT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def process_ach_import(self, import_type):
        """POST /mobilews/commercial/achImport/{type}

        :param str import_type: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.ACH_IMPORT_TYPE.value.format(type=import_type)
        return self._post(url=self._build_url(endpoint))

    def transform_ach(self, request_body):
        """POST /mobilews/commercial/achTransform

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.ACH_TRANSFORM.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_currency_codes(self):
        """GET /mobilews/commercial/currencyCode

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.CURRENCY_CODE.value
        return self._get(url=self._build_url(endpoint))

    def create_multi_domestic_wire(self, request_body):
        """POST /mobilews/commercial/draft/multiDomesticWire

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_DOMESTIC_WIRE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_multi_funds_transfer(self, request_body):
        """POST /mobilews/commercial/draft/multiFundsTransfer

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_FUNDS_TRANSFER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_multi_international_wire(self, request_body):
        """POST /mobilews/commercial/draft/multiInternationalWire

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_INTERNATIONAL_WIRE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_commercial_draft(self, draft_type, request_body):
        """POST /mobilews/commercial/draft/{type}

        :param str draft_type: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.DRAFT.value.format(type=draft_type)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_commercial_recurring_draft(self, draft_type, request_body):
        """POST /mobilews/commercial/draftRecurring/{type}

        :param str draft_type: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECURRING_DRAFT.value.format(type=draft_type)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_commercial_multi_template(self, request_body):
        """POST /mobilews/commercial/multiTemplate

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_TEMPLATE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_commercial_multi_template(self, template_id):
        """GET /mobilews/commercial/multiTemplate/{id}

        :param str template_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_ID.value.format(id=template_id)
        return self._get(url=self._build_url(endpoint))

    def update_commercial_multi_template(self, template_id, request_body):
        """PUT /mobilews/commercial/multiTemplate/{id}

        :param str template_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_ID.value.format(id=template_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def create_commercial_multi_template_payment(self, template_id, request_body):
        """POST /mobilews/commercial/multiTemplate/{id}/payment

        :param str template_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_PAYMENT.value.format(id=template_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_commercial_multi_template_payment(self, template_id, payment_id, request_body):
        """PUT /mobilews/commercial/multiTemplate/{id}/{paymentId}

        :param str template_id: path parameter
        :param str payment_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_PAYMENT_ID.value.format(id=template_id, paymentId=payment_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_commercial_multi_template_payment(self, template_id, payment_id):
        """DELETE /mobilews/commercial/multiTemplate/{id}/{paymentId}

        :param str template_id: path parameter
        :param str payment_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_PAYMENT_ID.value.format(id=template_id, paymentId=payment_id)
        return self._delete(url=self._build_url(endpoint))

    def get_recipients(self):
        """GET /mobilews/commercial/recipient

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT.value
        return self._get(url=self._build_url(endpoint))

    def create_recipient(self, request_body):
        """POST /mobilews/commercial/recipient

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_recipient_account(self, request_body):
        """PUT /mobilews/commercial/recipient/account

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_ACCOUNT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_recipient_account(self, account_id):
        """DELETE /mobilews/commercial/recipient/account/{id}

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_ACCOUNT_ID.value.format(id=account_id)
        return self._delete(url=self._build_url(endpoint))

    def get_recipient_account_pending(self, account_id):
        """GET /mobilews/commercial/recipient/account/{id}/pending

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_ACCOUNT_ID_PENDING.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_recipient_form(self):
        """GET /mobilews/commercial/recipient/form

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_recipient(self, recipient_id):
        """GET /mobilews/commercial/recipient/{id}

        :param str recipient_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_ID.value.format(id=recipient_id)
        return self._get(url=self._build_url(endpoint))

    def delete_recipient(self, recipient_id):
        """DELETE /mobilews/commercial/recipient/{id}

        :param str recipient_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_ID.value.format(id=recipient_id)
        return self._delete(url=self._build_url(endpoint))

    def update_recipient(self, recipient_id, request_body):
        """PUT /mobilews/commercial/recipient/{id}

        :param str recipient_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_ID.value.format(id=recipient_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_recipient_account_transactions(self, recipient_id, account_id):
        """GET /mobilews/commercial/recipient/{id}/account/{accountId}/transaction

        :param str recipient_id: path parameter
        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_ACCOUNT_TRANSACTION.value.format(id=recipient_id, accountId=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_recipient_transactions(self, recipient_id):
        """GET /mobilews/commercial/recipient/{id}/transaction

        :param str recipient_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.RECIPIENT_TRANSACTION.value.format(id=recipient_id)
        return self._get(url=self._build_url(endpoint))

    def get_subsidiaries(self):
        """GET /mobilews/commercial/subsidiary

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.SUBSIDIARY.value
        return self._get(url=self._build_url(endpoint))

    def create_subsidiary(self, request_body):
        """POST /mobilews/commercial/subsidiary

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.SUBSIDIARY.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_subsidiary_form(self):
        """GET /mobilews/commercial/subsidiary/form

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.SUBSIDIARY_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_subsidiary(self, subsidiary_id):
        """GET /mobilews/commercial/subsidiary/{id}

        :param str subsidiary_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.SUBSIDIARY_ID.value(id=subsidiary_id)
        return self._get(url=self._build_url(endpoint))

    def delete_subsidiary(self, subsidiary_id):
        """DELETE /mobilews/commercial/subsidiary/{id}

        :param str subsidiary_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.SUBSIDIARY_ID.value(id=subsidiary_id)
        return self._delete(url=self._build_url(endpoint))

    def update_subsidiary(self, subsidiary_id, request_body):
        """PUT /mobilews/commercial/subsidiary/{id}

        :param str subsidiary_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.SUBSIDIARY_ID.value(id=subsidiary_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_tax_payments(self):
        """GET /mobilews/commercial/taxpayment

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TAX_PAYMENT.value
        return self._get(url=self._build_url(endpoint))

    def get_tax_payment(self, short_name):
        """GET /mobilews/commercial/taxpayment/{shortName}

        :param str short_name: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TAX_PAYMENT_SHORT_NAME.value.format(shortName=short_name)
        return self._get(url=self._build_url(endpoint))

    def get_templates(self):
        """GET /mobilews/commercial/template

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TEMPLATE.value
        return self._get(url=self._build_url(endpoint))

    def create_favorite_template(self, template_id):
        """POST /mobilews/commercial/template/favorite/{id}

        :param str template_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TEMPLATE_FAVORITE.value.format(id=template_id)
        return self._post(url=self._build_url(endpoint))

    def delete_favorite_template(self, template_id):
        """DELETE /mobilews/commercial/template/favorite/{id}

        :param str template_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TEMPLATE_FAVORITE.value.format(id=template_id)
        return self._delete(url=self._build_url(endpoint))

    def get_template(self, template_id):
        """GET /mobilews/commercial/template/{id}

        :param str template_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TEMPLATE_ID.value.format(id=template_id)
        return self._get(url=self._build_url(endpoint))

    def delete_template(self, template_id):
        """DELETE /mobilews/commercial/template/{id}

        :param str template_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TEMPLATE_ID.value.format(id=template_id)
        return self._delete(url=self._build_url(endpoint))

    def update_template(self, template_id, request_body):
        """PUT /mobilews/commercial/template/{id}

        :param str template_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TEMPLATE_ID.value.format(id=template_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def create_template(self, transaction_type, request_body):
        """POST /mobilews/commercial/template/{transactionType}

        :param str transaction_type: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.TEMPLATE_TRANSACTION_TYPE.value.format(transactionType=transaction_type)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_users(self):
        """GET /mobilews/commercial/users

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CommercialEndpoint.USERS.value
        return self._get(url=self._build_url(endpoint))
