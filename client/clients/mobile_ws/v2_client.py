from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import V2Endpoint


class V2Client(BaseQ2Client):

    def get_commercial_tax_payments(self):
        """GET /mobilews/v2/commercial/taxpayment

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = V2Endpoint.COMMERCIAL_TAX_PAYMENT.value
        return self._get(url=self._build_url(endpoint))

    def get_commercial_tax_payment(self, tax_payment_id):
        """GET /mobilews/v2/commercial/taxpayment/{id}

        :param str tax_payment_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = V2Endpoint.COMMERCIAL_TAX_PAYMENT_ID.value.format(id=tax_payment_id)
        return self._get(url=self._build_url(endpoint))
