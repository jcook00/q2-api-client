from enum import Enum


class BackOfficeEndpoint(Enum):

    ADDRESS = "/hq/backOffice/address"
    ADDRESS_ID = "/hq/backOffice/address/{id}"
    ADMIN_USER = "/hq/backOffice/adminUser"
    ADMIN_USER_ID = "/hq/backOffice/adminUser/{id}"
    CSR_NOTE = "/hq/backOffice/csrNote"
    CSR_NOTE_ID = "/hq/backOffice/csrNote/{id}"
    CUSTOMER = "/hq/backOffice/customer"
    SUBSIDIARY = "/hq/backOffice/customer/{customerID}/subsidiary"
    SUBSIDIARY_ID = "/hq/backOffice/customer/{customerID}/subsidiary/{id}"
    CUSTOMER_ID = "/hq/backOffice/customer/{id}"
    GROUP_DETAIL = "/hq/backOffice/groupDetail"
    GROUP_DETAIL_ID = "/hq/backOffice/groupDetail/{id}"
    HOST_ACCOUNT = "/hq/backOffice/hostAccount"
    HOST_ACCOUNT_ID = "/hq/backOffice/hostAccount/{id}"
    SERVICE_CHARGE_PLAN = "/hq/backOffice/serviceChargePlan"
    SERVICE_CHARGE_PLAN_ID = "/hq/backOffice/serviceChargePlan/{id}"
    SYSTEM_PROPERTY = "/hq/backOffice/systemProperty"
    SYSTEM_PROPERTY_ID = "/hq/backOffice/systemProperty/{id}"
    CONFIG_PROPERTY_DATA = "/hq/backOffice/uIConfigPropertyData"
    CONFIG_PROPERTY_DATA_ID = "/hq/backOffice/uIConfigPropertyData/{id}"
    USER = "/hq/backOffice/user"
    USER_ID = "/hq/backOffice/user/{id}"
    USER_EMAIL = "/hq/backOffice/user/{userID}/email"
    USER_PHONE = "/hq/backOffice/user/{userID}/phone"
    USER_SAC_TARGETS = "/hq/backOffice/user/{userID}/sacTargets"
    USER_LOGON = "/hq/backOffice/userLogon"
    USER_LOGON_ID = "/hq/backOffice/userLogon/{id}"
    USER_LOGON_ACCESS_CODES = "/hq/backOffice/userLogon/{userLogonID}/accessCodes"
    USER_ROLE = "/hq/backOffice/userRole"
    USER_ROLE_ID = "/hq/backOffice/userRole/{id}"


class CoreEndpoint(Enum):

    BAI_CODES = "/hq/core/baiCodes"
    BAI_CODES_ID = "/hq/core/baiCodes/{id}"
    COUNTRY = "/hq/core/country"
    COUNTRY_ID = "/hq/core/country/{id}"
    DISPUTE_FORM_SHORT_NAME = "/hq/core/disputeForm/{languageShortName}"
    GOALS_CATEGORY_MAPPING = "/hq/core/goalsCategoryMapping/{id}"
    PASSWORD_POLICY = "/hq/core/passwordPolicy"
    PASSWORD_POLICY_ID = "/hq/core/passwordPolicy/{id}"
    PRODUCT_AND_TYPE = "/hq/core/productAndType"
    PRODUCT_AND_TYPE_ID = "/hq/core/productAndType/{id}"
    STATE = "/hq/core/state"
    STATE_ID = "/hq/core/state/{id}"
    TOKEN_INFO = "/hq/core/tokeninfo"


class FrontEndEndpoint(Enum):

    DISPUTE_FORM = "/hq/frontEnd/disputeForm"
    DISPUTE_ACCOUNT_ID = "/hq/frontEnd/disputes/{accountId}"
    DISPUTE_ID = "/hq/frontEnd/disputes/{accountId}/{disputeId}"
    HADE_HISTORY = "/hq/frontEnd/hadeHistory/{accountId}"


class TokenEndpoint(Enum):

    TOKEN_INFO = "/hq/tokeninfo"
