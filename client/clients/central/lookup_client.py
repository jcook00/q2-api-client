from client.clients.q2_client import Q2Client
from client.endpoints.central import LookupEndpoint


class LookupClient(Q2Client):

    def get_customer(self, customer_id):
        endpoint = LookupEndpoint.CUSTOMER_ID.value.format(customerId=customer_id)
        return self._get(url=self._build_url(endpoint))

    def search_customers(self, q, **query):
        endpoint = LookupEndpoint.SEARCH.value
        query_parameters = self._copy_query_parameters()
        query_parameters['q'] = q
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def sort_fields(self, sort_option_type):
        endpoint = LookupEndpoint.SORT_FIELDS.value
        query_parameters = self._copy_query_parameters()
        query_parameters['type'] = sort_option_type
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def get_user(self, user_id):
        endpoint = LookupEndpoint.USER_ID.value.format(userId=user_id)
        return self._get(url=self._build_url(endpoint))

    def get_user_logon(self, user_logon_id, fixture=None):
        endpoint = LookupEndpoint.USER_LOGON.value.format(userlogonId=user_logon_id)
        query_parameters = self._copy_query_parameters()
        query_parameters['fixture'] = fixture
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)
