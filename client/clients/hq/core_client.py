from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.hq_endpoints import CoreEndpoint


class CoreClient(BaseQ2Client):

    def get_bai_codes(self):
        """GET /hq/core/baiCodes

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.BAI_CODES.value
        return self._get(url=self._build_url(endpoint))

    def get_bai_code(self, bai_code_id):
        """GET /hq/core/baiCodes/{id}

        :param int bai_code_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.BAI_CODES_ID.value.format(id=bai_code_id)
        return self._get(url=self._build_url(endpoint))

    def get_countries(self):
        """GET /hq/core/country

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.COUNTRY.value
        return self._get(url=self._build_url(endpoint))

    def get_country(self, country_id):
        """GET /hq/core/country/{id}

        :param int country_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.COUNTRY_ID.value.format(id=country_id)
        return self._get(url=self._build_url(endpoint))

    def get_dispute_form(self, language_short_name):
        """GET /hq/core/disputeForm/{languageShortName}

        :param str language_short_name: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.DISPUTE_FORM_SHORT_NAME.value.format(languageShortName=language_short_name)
        return self._get(url=self._build_url(endpoint))

    def get_goals_category_mapping(self, mapping_id):
        """GET /hq/core/goalsCategoryMapping/{id}

        :param int mapping_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.GOALS_CATEGORY_MAPPING.value.format(id=mapping_id)
        return self._get(url=self._build_url(endpoint))

    def get_password_policies(self):
        """GET /hq/core/passwordPolicy

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.PASSWORD_POLICY.value
        return self._get(url=self._build_url(endpoint))

    def get_password_policy(self, policy_id):
        """GET /hq/core/passwordPolicy/{id}

        :param str policy_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.PASSWORD_POLICY_ID.value.format(id=policy_id)
        return self._get(url=self._build_url(endpoint))

    def get_products_and_types(self):
        """GET /hq/core/productAndType

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.PRODUCT_AND_TYPE.value
        return self._get(url=self._build_url(endpoint))

    def get_product_and_type(self, product_id):
        """GET /hq/core/productAndType/{id}

        :param str product_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.PRODUCT_AND_TYPE_ID.value.format(id=product_id)
        return self._get(url=self._build_url(endpoint))

    def get_states(self):
        """GET /hq/core/state

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.STATE.value
        return self._get(url=self._build_url(endpoint))

    def get_state(self, state_id):
        """GET /hq/core/state/{id}

        :param str state_id: path parameter
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.STATE_ID.value.format(id=state_id)
        return self._get(url=self._build_url(endpoint))

    def get_core_token_info(self):
        """GET /hq/core/tokeninfo

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = CoreEndpoint.TOKEN_INFO.value
        return self._get(url=self._build_url(endpoint))
