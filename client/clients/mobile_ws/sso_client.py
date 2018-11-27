from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import SSOEndpoint


class SSOClient(BaseQ2Client):

    def get_sso_bill_pay(self):
        """GET /mobilews/sso/billpay

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SSOEndpoint.SSO_BILL_PAY.value
        return self._get(url=self._build_url(endpoint))

    def get_sso_bill_pay_config(self, bill_pay_id):
        """GET /mobilews/sso/billpay/{id}

        :param str bill_pay_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SSOEndpoint.SSO_BILL_PAY_ID.value.format(id=bill_pay_id)
        return self._get(url=self._build_url(endpoint))

    def get_sso_generic_account_config(self, bill_pay_id, account_id):
        """GET /mobilews/sso/generic/{id}/{accountId}

        :param str bill_pay_id: path parameter
        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SSOEndpoint.SSO_GENERIC_ID.value.format(id=bill_pay_id, accountId=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_sso_generic_vendor_config(self, vendor_id):
        """GET /mobilews/sso/vendor/{id}

        :param str vendor_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SSOEndpoint.SSO_VENDOR_ID.value.format(id=vendor_id)
        return self._get(url=self._build_url(endpoint))
