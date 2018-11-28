from enum import Enum


class BankingEndpoint(Enum):

    ACCOUNT_STATUS_SHORT_NAME = "/v2/banking/accounts/{id}/statusShortName"
    GROUPS = "/v2/banking/groups"
    GROUP_ID = "/v2/banking/groups/{group_id}"


class CommercialEndpoint(Enum):

    CONFIG = "/v2/commercial/config"
    PAYMENTS = "/v2/commercial/payments"
    ACH_RULE = "/v2/commercial/positive-pay/ach-rule"
    ADD_CHECK = "/v2/commercial/positive-pay/add-check"
    EXCEPTION_ACCOUNTS = "/v2/commercial/positive-pay/exception-accounts/{vendorId}"
    EXCEPTION_DETAILS = "/v2/commercial/positive-pay/exception-details/{vendorId}/{transactionId}"
    EXCEPTIONS = "/v2/commercial/positive-pay/exceptions"
    EXCEPTIONS_ID = "/v2/commercial/positive-pay/exceptions/{vendorId}"
    RECIPIENTS = "/v2/commercial/recipients"
    RECIPIENT_ID = "/v2/commercial/recipients/{recipientId}"
    WIRES = "/v2/commercial/wires"
    WIRES_FX_RATE = "/v2/commercial/wires/fx-rate"


class PFMEndpoint(Enum):

    ACCOUNT_GUID = "/v2/pfm/accounts/{accountGuid}"
    CATEGORIES = "/v2/pfm/categories"
    CATEGORY_GUID = "/v2/pfm/categories/{categoryGuid}"
    INSTITUTIONS = "/v2/pfm/institutions"
    INSTITUTION_GUID = "/v2/pfm/institutions/{institutionGuid}"
    INSTITUTION_CREDENTIALS = "/v2/pfm/institutions/{institutionGuid}/credentials"
    JOB = "/v2/pfm/jobs/{jobGuid}"
    JOB_MFA_CREDENTIALS = "/v2/pfm/jobs/{jobGuid}/mfa_credentials"
    JOB_RESUME = "/v2/pfm/jobs/{jobGuid}/resume"
    MEMBERS = "/v2/pfm/members/"
    ALL_MEMBERS = "/v2/pfm/members/all"
    MEMBER_GUID = "/v2/pfm/members/{memberGuid}"
    MEMBER_CREDENTIALS = "/v2/pfm/members/{memberGuid}/credentials"
    MEMBER_REFRESH = "/v2/pfm/members/{memberGuid}/refresh"
    TRANSACTION_GUID = "/v2/pfm/transactions/{transactionGuid}"
    TRANSACTION_SPLITS = "/v2/pfm/transactions/{transactionGuid}/splits"
    USERS = "/v2/pfm/users"
    WIDGET = "/v2/pfm/widgets/{widgetShortName}"
