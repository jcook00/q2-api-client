from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.central_endpoints import LookupEndpoint


class LookupClient(BaseQ2Client):

    def get_customer(self, customer_id, fixture=None):
        """GET /central/lookup/customer/{customerId}

        :param int customer_id: path parameter
        :param bool fixture: fixture query parameter
            (If true, will return hardcoded values and not call HQ)
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LookupEndpoint.CUSTOMER_ID.value.format(customerId=customer_id)
        query_parameters = self._copy_query_parameters()
        query_parameters['fixture'] = fixture
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def search_customers(self, q, **query):
        """GET /central/lookup/search

        :param str q: query parameter
            (Characters that will be used to perform a 'begins with' search)
        :param dict query: additional query parameters
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LookupEndpoint.SEARCH.value
        query_parameters = self._copy_query_parameters()
        query_parameters['q'] = q
        query_parameters.update(**query)
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def sort_fields(self, sort_option_type):
        """GET /central/lookup/sort-fields

        :param str sort_option_type: query parameter
            (The type for which the sort fields will be returned)
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LookupEndpoint.SORT_FIELDS.value
        query_parameters = self._copy_query_parameters()
        query_parameters['type'] = sort_option_type
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def get_user(self, user_id, fixture=None):
        """GET /central/lookup/user/{userId}

        :param int user_id: path parameter
        :param bool fixture: fixture query parameter
            (If true, will return hardcoded values and not call HQ)
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LookupEndpoint.USER_ID.value.format(userId=user_id)
        query_parameters = self._copy_query_parameters()
        query_parameters['fixture'] = fixture
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)

    def get_user_logon(self, user_logon_id, fixture=None):
        """GET /central/lookup/userlogon/{userlogonId}

        :param int user_logon_id: path parameter
        :param bool fixture: fixture query parameter
            (If true, will return hardcoded values and not call HQ)
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LookupEndpoint.USER_LOGON.value.format(userlogonId=user_logon_id)
        query_parameters = self._copy_query_parameters()
        query_parameters['fixture'] = fixture
        return self._get(url=self._build_url(endpoint), query_parameters=query_parameters)
