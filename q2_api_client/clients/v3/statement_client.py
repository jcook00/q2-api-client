from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import StatementEndpoint


class StatementClient(BaseQ2Client):

    def get_statement(self, key):
        """GET /v3/statement/{key}

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = StatementEndpoint.STATEMENT_KEY.value.format(key=key)
        return self._get(url=self._build_url(endpoint))

    def retrieve_statements(self, request_body):
        """POST /v3/statement/retrieve

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = StatementEndpoint.RETRIEVE_STATEMENTS.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def generate_statement_url(self, statement_id):
        """POST /v3/statement/{id}/generateUrl

        :param str statement_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = StatementEndpoint.GENERATE_STATEMENT_URL.value.format(id=statement_id)
        return self._post(url=self._build_url(endpoint))
