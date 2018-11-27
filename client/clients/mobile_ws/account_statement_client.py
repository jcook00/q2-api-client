from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AccountStatementEndpoint


class AccountStatementClient(BaseQ2Client):

    def get_account_statement_form(self):
        """GET /mobilews/accountStatement/form

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountStatementEndpoint.ACCOUNT_STATEMENT_FORM.value
        return self._get(url=self._build_url(endpoint))

    def get_account_statement(self, account_id):
        """GET /mobilews/accountStatement/{id}

        :param str account_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountStatementEndpoint.ACCOUNT_STATEMENT_ID.value.format(id=account_id)
        return self._get(url=self._build_url(endpoint))

    def get_account_statement_image(self, account_id, image_id, image_type):
        """GET /mobilews/accountStatement/{id}/{imageId}/{imageType}

        :param str account_id: path parameter
        :param str image_id: path parameter
        :param str image_type: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AccountStatementEndpoint.IMAGE_TYPE.value.format(id=account_id, imageId=image_id, imageType=image_type)
        return self._get(url=self._build_url(endpoint))
