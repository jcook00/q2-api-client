from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import CustomerEndpoint


class CustomerClient(BaseQ2Client):

    def retrieve_customers(self, request_body):
        """POST /backoffice/v3/customer/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CustomerEndpoint.RETRIEVE_CUSTOMERS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def retrieve_customer(self, customer_id):
        """POST /backoffice/v3/customer/{id}/retrieve

        :param str customer_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CustomerEndpoint.RETRIEVE_CUSTOMER.value.format(id=customer_id)
        return self._post(url=self._build_url(endpoint))
