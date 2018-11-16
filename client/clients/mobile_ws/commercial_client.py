from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import CommercialEndpoint


class CommercialClient(BaseQ2Client):

    def reprocess_ach_import(self, **request_body):
        endpoint = CommercialEndpoint.ACH_IMPORT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def process_ach_import(self, import_type):
        endpoint = CommercialEndpoint.ACH_IMPORT_TYPE.value.format(type=import_type)
        return self._post(url=self._build_url(endpoint))

    def transform_ach(self, **request_body):
        endpoint = CommercialEndpoint.ACH_TRANSFORM.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_currency_codes(self):
        endpoint = CommercialEndpoint.CURRENCY_CODE.value
        return self._get(url=self._build_url(endpoint))

    def create_multi_domestic_wire(self, **request_body):
        endpoint = CommercialEndpoint.MULTI_DOMESTIC_WIRE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_multi_funds_transfer(self, **request_body):
        endpoint = CommercialEndpoint.MULTI_FUNDS_TRANSFER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_multi_international_wire(self, **request_body):
        endpoint = CommercialEndpoint.MULTI_INTERNATIONAL_WIRE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_commercial_draft(self, draft_type, **request_body):
        endpoint = CommercialEndpoint.DRAFT.value.format(type=draft_type)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_commercial_recurring_draft(self, draft_type, **request_body):
        endpoint = CommercialEndpoint.RECURRING_DRAFT.value.format(type=draft_type)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def create_commercial_multi_template(self, **request_body):
        endpoint = CommercialEndpoint.MULTI_TEMPLATE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_commercial_multi_template(self, template_id):
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_ID.value.format(id=template_id)
        return self._get(url=self._build_url(endpoint))

    def update_commercial_multi_template(self, template_id, **request_body):
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_ID.value.format(id=template_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def create_commercial_multi_template_payment(self, template_id, **request_body):
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_PAYMENT.value.format(id=template_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_commercial_multi_template_payment(self, template_id, payment_id, **request_body):
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_PAYMENT_ID.value.format(id=template_id, paymentId=payment_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_commercial_multi_template_payment(self, template_id, payment_id):
        endpoint = CommercialEndpoint.MULTI_TEMPLATE_PAYMENT_ID.value.format(id=template_id, paymentId=payment_id)
        return self._delete(url=self._build_url(endpoint))

    def get_recipients(self):
        endpoint = CommercialEndpoint.RECIPIENT.value
        return self._get(url=self._build_url(endpoint))

    def create_recipient(self, **request_body):
        endpoint = CommercialEndpoint.RECIPIENT.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_recipient_account(self, **request_body):
        endpoint = CommercialEndpoint.RECIPIENT_ACCOUNT.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_recipient_account(self, account_id):
        endpoint = CommercialEndpoint.RECIPIENT_ACCOUNT_ID.value.format(id=account_id)
        return self._delete(url=self._build_url(endpoint))

    def get_recipient_account_pending(self, account_id):
        endpoint = CommercialEndpoint.RECIPIENT_ACCOUNT_ID_PENDING.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_recipient_form(self):
        endpoint = CommercialEndpoint.RECIPIENT_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_recipient(self, recipient_id):
        endpoint = CommercialEndpoint.RECIPIENT_ID.value.format(id=recipient_id)
        return self._get(url=self._build_url(endpoint))

    def delete_recipient(self, recipient_id):
        endpoint = CommercialEndpoint.RECIPIENT_ID.value.format(id=recipient_id)
        return self._delete(url=self._build_url(endpoint))

    def update_recipient(self, recipient_id, **request_body):
        endpoint = CommercialEndpoint.RECIPIENT_ID.value.format(id=recipient_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_recipient_account_transactions(self, recipient_id, account_id):
        endpoint = CommercialEndpoint.RECIPIENT_ACCOUNT_TRANSACTION.value.format(id=recipient_id, accountId=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_recipient_transactions(self, recipient_id):
        endpoint = CommercialEndpoint.RECIPIENT_TRANSACTION.value.format(id=recipient_id)
        return self._get(url=self._build_url(endpoint))

    def get_subsidiaries(self):
        endpoint = CommercialEndpoint.SUBSIDIARY.value
        return self._get(url=self._build_url(endpoint))

    def create_subsidiary(self, **request_body):
        endpoint = CommercialEndpoint.SUBSIDIARY.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_subsidiary_form(self):
        endpoint = CommercialEndpoint.SUBSIDIARY_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_subsidiary(self, subsidiary_id):
        endpoint = CommercialEndpoint.SUBSIDIARY_ID.value(id=subsidiary_id)
        return self._get(url=self._build_url(endpoint))

    def delete_subsidiary(self, subsidiary_id):
        endpoint = CommercialEndpoint.SUBSIDIARY_ID.value(id=subsidiary_id)
        return self._delete(url=self._build_url(endpoint))

    def update_subsidiary(self, subsidiary_id, **request_body):
        endpoint = CommercialEndpoint.SUBSIDIARY_ID.value(id=subsidiary_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_tax_payments(self):
        endpoint = CommercialEndpoint.TAX_PAYMENT.value
        return self._get(url=self._build_url(endpoint))

    def get_tax_payment(self, short_name):
        endpoint = CommercialEndpoint.TAX_PAYMENT_SHORT_NAME.value.format(shortName=short_name)
        return self._get(url=self._build_url(endpoint))

    def get_templates(self):
        endpoint = CommercialEndpoint.TEMPLATE.value
        return self._get(url=self._build_url(endpoint))

    def create_favorite_template(self, template_id):
        endpoint = CommercialEndpoint.TEMPLATE_FAVORITE.value.format(id=template_id)
        return self._post(url=self._build_url(endpoint))

    def delete_favorite_template(self, template_id):
        endpoint = CommercialEndpoint.TEMPLATE_FAVORITE.value.format(id=template_id)
        return self._delete(url=self._build_url(endpoint))

    def get_template(self, template_id):
        endpoint = CommercialEndpoint.TEMPLATE_ID.value.format(id=template_id)
        return self._get(url=self._build_url(endpoint))

    def delete_template(self, template_id):
        endpoint = CommercialEndpoint.TEMPLATE_ID.value.format(id=template_id)
        return self._delete(url=self._build_url(endpoint))

    def update_template(self, template_id, **request_body):
        endpoint = CommercialEndpoint.TEMPLATE_ID.value.format(id=template_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def create_template(self, transaction_type, **request_body):
        endpoint = CommercialEndpoint.TEMPLATE_TRANSACTION_TYPE.value.format(transactionType=transaction_type)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_users(self):
        endpoint = CommercialEndpoint.USERS.value
        return self._get(url=self._build_url(endpoint))
