from client.clients.q2_client import Q2Client
from client.endpoints.hq import CoreEndpoint


class CoreClient(Q2Client):

    def get_bai_codes(self):
        endpoint = CoreEndpoint.BAI_CODES.value
        return self.get(url=self.build_url(endpoint))

    def get_bai_code(self, bai_code_id):
        endpoint = CoreEndpoint.BAI_CODES_ID.value.format(id=bai_code_id)
        return self.get(url=self.build_url(endpoint))

    def get_countries(self):
        endpoint = CoreEndpoint.COUNTRY.value
        return self.get(url=self.build_url(endpoint))

    def get_country(self, country_id):
        endpoint = CoreEndpoint.COUNTRY_ID.value.format(id=country_id)
        return self.get(url=self.build_url(endpoint))

    def get_dispute_form(self, language_short_name):
        endpoint = CoreEndpoint.DISPUTE_FORM_SHORT_NAME.value.format(languageShortName=language_short_name)
        return self.get(url=self.build_url(endpoint))

    def get_goals_category_mapping(self, mapping_id):
        endpoint = CoreEndpoint.GOALS_CATEGORY_MAPPING.value.format(id=mapping_id)
        return self.get(url=self.build_url(endpoint))

    def get_password_policies(self):
        endpoint = CoreEndpoint.PASSWORD_POLICY.value
        return self.get(url=self.build_url(endpoint))

    def get_password_policy(self, policy_id):
        endpoint = CoreEndpoint.PASSWORD_POLICY_ID.value.format(id=policy_id)
        return self.get(url=self.build_url(endpoint))

    def get_products_and_types(self):
        endpoint = CoreEndpoint.PRODUCT_AND_TYPE.value
        return self.get(url=self.build_url(endpoint))

    def get_product_and_type(self, product_id):
        endpoint = CoreEndpoint.PRODUCT_AND_TYPE_ID.value.format(id=product_id)
        return self.get(url=self.build_url(endpoint))

    def get_states(self):
        endpoint = CoreEndpoint.STATE.value
        return self.get(url=self.build_url(endpoint))

    def get_state(self, state_id):
        endpoint = CoreEndpoint.STATE_ID.value.format(id=state_id)
        return self.get(url=self.build_url(endpoint))

    def get_core_token_info(self):
        endpoint = CoreEndpoint.TOKEN_INFO.value
        return self.get(url=self.build_url(endpoint))
