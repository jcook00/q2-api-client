from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.hq_endpoints import FrontEndEndpoint


class FrontEndClient(BaseQ2Client):

    def get_dispute_form(self):
        """GET /hq/frontEnd/disputeForm

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FrontEndEndpoint.DISPUTE_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_dispute(self, account_id, dispute_id):
        """GET /hq/frontEnd/disputes/{accountId}/{disputeId}

        :param int account_id: path parameter
        :param str dispute_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FrontEndEndpoint.DISPUTE_ID.value.format(accountId=account_id, disputeId=dispute_id)
        return self._get(url=self._build_url(endpoint))

    def create_dispute(self, account_id, request_body):
        """POST /hq/frontEnd/disputes/{accountId}

        :param int account_id: path parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FrontEndEndpoint.DISPUTE_ACCOUNT_ID.value.format(accountId=account_id)
        return self._post(url=self._build_url(endpoint), json=request_body)

    def delete_dispute(self, account_id, dispute_id):
        """DELETE /hq/frontEnd/disputes/{accountId}/{disputeId}

        :param int account_id: path parameter
        :param str dispute_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FrontEndEndpoint.DISPUTE_ID.value.format(accountId=account_id, disputeId=dispute_id)
        return self._delete(url=self._build_url(endpoint))

    def get_hade_history(self, account_id):
        """GET /hq/frontEnd/hadeHistory/{accountId}

        :param int account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FrontEndEndpoint.HADE_HISTORY.value.format(accountId=account_id)
        return self._get(url=self._build_url(endpoint))
