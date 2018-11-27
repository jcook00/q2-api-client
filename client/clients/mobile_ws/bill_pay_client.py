from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import BillPayEndpoint


class BillPayClient(BaseQ2Client):

    def get_bill_pay_vendor_account(self, vendor_id):
        """GET /mobilews/billpay/{vendorId}/account

        :param str vendor_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.ACCOUNT.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def create_bill_pay_vendor_account(self, vendor_id, request_body):
        """POST /mobilews/billpay/{vendorId}/account

        :param str vendor_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.ACCOUNT.value.format(vendorId=vendor_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_bill_pay_vendor_account(self, vendor_id, request_body):
        """PUT /mobilews/billpay/{vendorId}/account

        :param str vendor_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.ACCOUNT.value.format(vendorId=vendor_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_bill_pay_vendor_account_id(self, vendor_id, account_id):
        """GET /mobilews/billpay/{vendorId}/account/{accountId}

        :param str vendor_id: path parameter
        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.ACCOUNT_ID.value.format(vendorId=vendor_id, accountId=account_id)
        return self._get(url=self._build_url(endpoint))

    def delete_bill_pay_vendor_account_id(self, vendor_id, account_id):
        """DELETE /mobilews/billpay/{vendorId}/account/{accountId}

        :param str vendor_id: path parameter
        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.ACCOUNT_ID.value.format(vendorId=vendor_id, accountId=account_id)
        return self._delete(url=self._build_url(endpoint))

    def update_bill_pay_vendor_account_id(self, vendor_id, account_id, request_body):
        """PUT /mobilews/billpay/{vendorId}/account/{accountId}

        :param str vendor_id: path parameter
        :param str account_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.ACCOUNT_ID.value.format(vendorId=vendor_id, accountId=account_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_bill_pay_vendor_config(self, vendor_id):
        """GET /mobilews/billpay/{vendorId}/config

        :param str vendor_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.CONFIG.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def get_bill_pay_vendor_ebill(self, vendor_id):
        """GET /mobilews/billpay/{vendorId}/ebill

        :param str vendor_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def create_bill_pay_vendor_ebill_autopay(self, vendor_id, request_body):
        """POST /mobilews/billpay/{vendorId}/ebill/autopay

        :param str vendor_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL_AUTOPAY.value.format(vendorId=vendor_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_bill_pay_vendor_ebill_autopay_biller_id(self, vendor_id, biller_id, request_body):
        """PUT /mobilews/billpay/{vendorId}/ebill/autopay/{billerId}

        :param str vendor_id: path parameter
        :param str biller_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL_AUTOPAY_BILLER_ID.value.format(vendorId=vendor_id, billerId=biller_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_bill_pay_vendor_ebill_autopay_biller_id(self, vendor_id, payee_id, biller_id):
        """DELETE /mobilews/billpay/{vendorId}/ebill/autopay/{payeeId}/{billerId}

        :param str vendor_id: path parameter
        :param str payee_id: path parameter
        :param str biller_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL_AUTOPAY_PAYEE_ID.value.format(vendorId=vendor_id, payeeId=payee_id, billerId=biller_id)
        return self._delete(url=self._build_url(endpoint))

    def get_bill_pay_vendor_ebill_bill_id(self, vendor_id, bill_id):
        """GET /mobilews/billpay/{vendorId}/ebill/{billId}

        :param str vendor_id: path parameter
        :param str bill_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL_BILL_ID.value.format(vendorId=vendor_id, billId=bill_id)
        return self._get(url=self._build_url(endpoint))

    def update_bill_pay_vendor_ebill_bill_id(self, vendor_id, bill_id, request_body):
        """PUT /mobilews/billpay/{vendorId}/ebill/{billId}

        :param str vendor_id: path parameter
        :param str bill_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL_BILL_ID.value.format(vendorId=vendor_id, billId=bill_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def delete_bill_pay_vendor_ebill_bill_id(self, vendor_id, payee_id):
        """DELETE /mobilews/billpay/{vendorId}/ebill/{payeeId}

        :param str vendor_id: path parameter
        :param str payee_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL_PAYEE_ID.value.format(vendorId=vendor_id, payeeId=payee_id)
        return self._delete(url=self._build_url(endpoint))

    def create_bill_pay_vendor_ebill_bill_id(self, vendor_id, payee_id, request_body):
        """POST /mobilews/billpay/{vendorId}/ebill/{payeeId}

        :param str vendor_id: path parameter
        :param str payee_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL_PAYEE_ID.value.format(vendorId=vendor_id, payeeId=payee_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_bill_pay_vendor_ebill_account_id(self, vendor_id, payee_id, ebill_account_id):
        """DELETE /mobilews/billpay/{vendorId}/ebill/{payeeId}/{ebillaccountid}

        :param str vendor_id: path parameter
        :param str payee_id: path parameter
        :param str ebill_account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.EBILL_ACCOUNT_ID.value.format(vendorId=vendor_id, payeeId=payee_id, ebillaccountid=ebill_account_id)
        return self._delete(url=self._build_url(endpoint))

    def get_bill_pay_vendor_payee(self, vendor_id):
        """GET /mobilews/billpay/{vendorId}/payee

        :param str vendor_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYEE.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def create_bill_pay_vendor_payee(self, vendor_id, request_body):
        """POST /mobilews/billpay/{vendorId}/payee

        :param str vendor_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYEE.value.format(vendorId=vendor_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def get_bill_pay_vendor_payee_ebill_payee_id(self, vendor_id, payee_id):
        """GET /mobilews/billpay/{vendorId}/payee/ebill/{payeeId}

        :param str vendor_id: path parameter
        :param str payee_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYEE_EBILL_PAYEE_ID.value.format(vendorId=vendor_id, payeeId=payee_id)
        return self._get(url=self._build_url(endpoint))

    def get_bill_pay_vendor_payee_id(self, vendor_id, payee_id):
        """GET /mobilews/billpay/{vendorId}/payee/{payeeId}

        :param str vendor_id: path parameter
        :param str payee_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYEE_ID.value.format(vendorId=vendor_id, payeeId=payee_id)
        return self._get(url=self._build_url(endpoint))

    def delete_bill_pay_vendor_payee_id(self, vendor_id, payee_id):
        """DELETE /mobilews/billpay/{vendorId}/payee/{payeeId}

        :param str vendor_id: path parameter
        :param str payee_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYEE_ID.value.format(vendorId=vendor_id, payeeId=payee_id)
        return self._delete(url=self._build_url(endpoint))

    def update_bill_pay_vendor_payee_id(self, vendor_id, payee_id, request_body):
        """PUT /mobilews/billpay/{vendorId}/payee/{payeeId}

        :param str vendor_id: path parameter
        :param str payee_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYEE_ID.value.format(vendorId=vendor_id, payeeId=payee_id)
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_bill_pay_vendor_payments(self, vendor_id):
        """GET /mobilews/billpay/{vendorId}/payment

        :param str vendor_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYMENT.value.format(vendorId=vendor_id)
        return self._get(url=self._build_url(endpoint))

    def create_bill_pay_vendor_payment(self, vendor_id, request_body):
        """POST /mobilews/billpay/{vendorId}/payment

        :param str vendor_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYMENT.value.format(vendorId=vendor_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_bill_pay_vendor_payment(self, vendor_id, payment_id):
        """DELETE /mobilews/billpay/{vendorId}/payment/{paymentId}

        :param str vendor_id: path parameter
        :param str payment_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYMENT_ID.value.format(vendorId=vendor_id, paymentId=payment_id)
        return self._delete(url=self._build_url(endpoint))

    def get_bill_pay_vendor_payment(self, vendor_id, payment_id):
        """GET /mobilews/billpay/{vendorId}/payment/{paymentId}

        :param str vendor_id: path parameter
        :param str payment_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.PAYMENT_ID.value.format(vendorId=vendor_id, paymentId=payment_id)
        return self._get(url=self._build_url(endpoint))

    def create_bill_pay_vendor_subscriber(self, vendor_id, request_body):
        """POST /mobilews/billpay/{vendorId}/subscriber

        :param str vendor_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = BillPayEndpoint.SUBSCRIBER.value.format(vendorId=vendor_id)
        return self._post(url=self._build_url(endpoint), json=request_body)
