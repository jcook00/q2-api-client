from enum import Enum


class AccessCodeEndpoint(Enum):

    ACCESS_CODE = "/mobilews/accessCode"
    ACCESS_CODE_VALIDATE = "/mobilews/accessCode/validate"
    ACCESS_CODE_VALIDATE_TOKEN = "/mobilews/accessCode/validateToken"


class AccountEndpoint(Enum):

    ACCOUNT = "/mobilews/account"
    ACCOUNT_SET_ENROLLED = "/mobilews/account/Pfm/setEnrolledToTrue"
    ACCOUNT_GROUP = "/mobilews/account/group"
    ACCOUNT_GROUP_ID = "/mobilews/account/group/{id}"
    ACCOUNT_LABEL = "/mobilews/account/label"
    ACCOUNT_LABEL_ID = "/mobilews/account/label/{id}"
    ACCOUNT_ID = "/mobilews/account/{id}"
    ACCOUNT_INQUIRY_LINK = "/mobilews/account/{id}/inquiryLink"
    ACCOUNT_HADE_ID = "/mobilews/account/{id}/{hadeId}"


class AccountExportEndpoint(Enum):

    ACCOUNT_EXPORT_FORMAT = "/mobilews/accountExport/{id}/{exportFormat}"


class AccountHistoryEndpoint(Enum):

    ACCOUNT_HISTORY_ID = "/mobilews/accountHistory/{id}"
    INQUIRY_LINK = "/mobilews/accountHistory/{id}/{transactionId}/{type}/inquiryLink"
    IMAGE_SEQUENCE_ID = "/mobilews/accountHistoryDetail/{Id}/{transactionId}/image/{sequenceId}"
    DETAIL_TRANSACTION_TYPE = "/mobilews/accountHistoryDetail/{id}/{transactionId}/{transactionType}"
    IMAGE_TRANSACTION_TYPE = "/mobilews/accountHistoryImage/{id}/{transactionId}/{transactionType}"
    IMAGE_NUMBER = "/mobilews/accountHistoryImage/{id}/{transactionId}/{transactionType}/{imageNumber}"


class AccountPFMEndpoint(Enum):

    ACCOUNT_PFM = "/mobilews/accountPfm"
    ACCOUNT_PFM_DATA = "/mobilews/accountPfm/data"
    ACCOUNT_PFM_ID = "/mobilews/accountPfm/{id}"
    ACCOUNT_PFM_HISTORY = "/mobilews/accountPfm/{id}/history"
    ACCOUNT_PFM_EXPORT = "/mobilews/accountPfmExport/{id}/{exportFormat}"


class AccountStatementEndpoint(Enum):

    ACCOUNT_STATEMENT_FORM = "/mobilews/accountStatement/form"
    ACCOUNT_STATEMENT_ID = "/mobilews/accountStatement/{id}"
    IMAGE_TYPE = "/mobilews/accountStatement/{id}/{imageId}/{imageType}"


class AccountsEndpoint(Enum):

    ACCOUNTS = "/mobilews/accounts"
    BLOCK_ACCOUNTS = "/mobilews/accounts/block"
    DELETE_ACCOUNTS = "/mobilews/accounts/delete"


class AdapterEndpoint(Enum):

    ADAPTER = "/mobilews/adapter/{vendorId}/{accountId}"


class AlertsEndpoint(Enum):

    ALERTS = "/mobilews/alerts"
    ALERTS_FORM = "/mobilews/alerts/form"
    ALERTS_FORM_TYPE = "/mobilews/alerts/form/{type}"
    ALERTS_ID = "/mobilews/alerts/{id}"
    ALERTS_TYPE = "/mobilews/alerts/{type}"


class AntiphishingEndpoint(Enum):

    ANTIPHISHING = "/mobilews/antiphishing"
    ANTIPHISHING_TOKEN = "/mobilews/antiphishing/{userToken}"


class AuditEndpoint(Enum):

    AUDIT = "/mobilews/audit"


class BillPayEndpoint(Enum):

    ACCOUNT = "/mobilews/billpay/{vendorId}/account"
    ACCOUNT_ID = "/mobilews/billpay/{vendorId}/account/{accountId}"
    CONFIG = "/mobilews/billpay/{vendorId}/config"
    EBILL = "/mobilews/billpay/{vendorId}/ebill"
    EBILL_AUTOPAY = "/mobilews/billpay/{vendorId}/ebill/autopay"
    EBILL_AUTOPAY_BILLER_ID = "/mobilews/billpay/{vendorId}/ebill/autopay/{billerId}"
    EBILL_AUTOPAY_PAYEE_ID = "/mobilews/billpay/{vendorId}/ebill/autopay/{payeeId}/{billerId}"
    EBILL_BILL_ID = "/mobilews/billpay/{vendorId}/ebill/{billId}"
    EBILL_PAYEE_ID = "/mobilews/billpay/{vendorId}/ebill/{payeeId}"
    EBILL_ACCOUNT_ID = "/mobilews/billpay/{vendorId}/ebill/{payeeId}/{ebillaccountid}"
    PAYEE = "/mobilews/billpay/{vendorId}/payee"
    PAYEE_EBILL_PAYEE_ID = "/mobilews/billpay/{vendorId}/payee/ebill/{payeeId}"
    PAYEE_ID = "/mobilews/billpay/{vendorId}/payee/{payeeId}"
    PAYMENT = "/mobilews/billpay/{vendorId}/payment"
    PAYMENT_ID = "/mobilews/billpay/{vendorId}/payment/{paymentId}"
    SUBSCRIBER = "/mobilews/billpay/{vendorId}/subscriber"


class CalendarEndpoint(Enum):

    CALENDAR = "/mobilews/calendar"
    CALENDAR_TRANSACTION_TYPE = "/mobilews/calendar/{transactionType}"


class SecurityEndpoint(Enum):

    CHANGE_PASSWORD = "/mobilews/changePassword"
    VALIDATE_PASSWORD = "/mobilews/validatePassword"


class CommercialEndpoint(Enum):

    ACH_IMPORT = "/mobilews/commercial/achImport"
    ACH_IMPORT_TYPE = "/mobilews/commercial/achImport/{type}"
    ACH_TRANSFORM = "/mobilews/commercial/achTransform"
    CURRENCY_CODE = "/mobilews/commercial/currencyCode"
    MULTI_DOMESTIC_WIRE = "/mobilews/commercial/draft/multiDomesticWire"
    MULTI_FUNDS_TRANSFER = "/mobilews/commercial/draft/multiFundsTransfer"
    MULTI_INTERNATIONAL_WIRE = "/mobilews/commercial/draft/multiInternationalWire"
    DRAFT = "/mobilews/commercial/draft/{type}"
    RECURRING_DRAFT = "/mobilews/commercial/draftRecurring/{type}"
    MULTI_TEMPLATE = "/mobilews/commercial/multiTemplate"
    MULTI_TEMPLATE_ID = "/mobilews/commercial/multiTemplate/{id}"
    MULTI_TEMPLATE_PAYMENT = "/mobilews/commercial/multiTemplate/{id}/payment"
    MULTI_TEMPLATE_PAYMENT_ID = "/mobilews/commercial/multiTemplate/{id}/{paymentId}"
    RECIPIENT = "/mobilews/commercial/recipient"
    RECIPIENT_ACCOUNT = "/mobilews/commercial/recipient/account"
    RECIPIENT_ACCOUNT_ID = "/mobilews/commercial/recipient/account/{id}"
    RECIPIENT_ACCOUNT_ID_PENDING = "/mobilews/commercial/recipient/account/{id}/pending"
    RECIPIENT_FORM = "/mobilews/commercial/recipient/form"
    RECIPIENT_ID = "/mobilews/commercial/recipient/{id}"
    RECIPIENT_ACCOUNT_TRANSACTION = "/mobilews/commercial/recipient/{id}/account/{accountId}/transaction"
    RECIPIENT_TRANSACTION = "/mobilews/commercial/recipient/{id}/transaction"
    SUBSIDIARY = "/mobilews/commercial/subsidiary"
    SUBSIDIARY_FORM = "/mobilews/commercial/subsidiary/form"
    SUBSIDIARY_ID = "/mobilews/commercial/subsidiary/{id}"
    TAX_PAYMENT = "/mobilews/commercial/taxpayment"
    TAX_PAYMENT_SHORT_NAME = "/mobilews/commercial/taxpayment/{shortName}"
    TEMPLATE = "/mobilews/commercial/template"
    TEMPLATE_FAVORITE = "/mobilews/commercial/template/favorite/{id}"
    TEMPLATE_ID = "/mobilews/commercial/template/{id}"
    TEMPLATE_TRANSACTION_TYPE = "/mobilews/commercial/template/{transactionType}"
    USERS = "/mobilews/commercial/users"


class CSREndpoint(Enum):

    CONFIG = "/mobilews/csr/config"
    CONFIG_NAME = "/mobilews/csr/config/{name}"
    CONFIG_NAME_PREFIXED = "/mobilews/csr/config/{name}/{prefixNameWithLoginDot}"
    DASHBOARD_ACTIVITY = "/mobilews/csr/dashboardActivity"
    NAV = "/mobilews/csr/nav"
    PROPERTIES = "/mobilews/csr/userProperties"


class DisclaimerEndpoint(Enum):

    DISCLAIMER = "/mobilews/disclaimer"
    DISCLAIMER_ID = "/mobilews/disclaimer/{id}"


class EDVEndpoint(Enum):

    EDV = "/mobilews/edv"


class FeedsEndpoint(Enum):

    FEEDS = "/mobilews/feeds/{type}"
    CHECKSUM = "/mobilews/feeds/{type}/{checksum}"


class FIEndpoint(Enum):

    FI = "/mobilews/fi"
    FI_WEDGE_LOOKUP = "/mobilews/fi/{wedgeLookupId}"


class FormEndpoint(Enum):

    FORM = "/mobilews/form"
    FORM_ID = "/mobilews/form/{id}"
    FORM_ACCOUNT_ID = "/mobilews/form/{id}/{accountId}"
    FORM_HADE_ID = "/mobilews/form/{id}/{accountId}/{hadeid}"
    FORM_UNAUTH = "/mobilews/formUnauth/{id}"


class FrontEndEndpoint(Enum):

    FRONT_END_CONFIG = "/mobilews/frontEndConfig"


class FSFEndpoint(Enum):

    FSF = "/mobilews/fsf"
    FSF_ATTACHMENT = "/mobilews/fsf/attachment"


class GAMEndpoint(Enum):

    LOOKUP = "/mobilews/gam/lookup"
    TEAM = "/mobilews/gam/team"
    TEAM_ID = "/mobilews/gam/team/{id}"
    USER_ID = "/mobilews/gam/user/{id}"


class KeepAliveEndpoint(Enum):

    KEEP_ALIVE = "/mobilews/keepalive"


class LanguageEndpoint(Enum):

    LANGUAGE = "/mobilews/language"


class LocationsEndpoint(Enum):

    LOCATIONS = "/mobilews/locations"
    ADDRESS = "/mobilews/locations/address/{address}"
    ADDRESS_LAT_LONG = "/mobilews/locations/address/{address}/{latitude}/{longitude}"
    LOCATIONS_LAT_LONG = "/mobilews/locations/{latitude}/{longitude}"


class LoginEndpoint(Enum):

    LOGIN_CSR = "/mobilews/logincsr"
    LOGOFF_USER = "/mobilews/logoffUser"
    LOGON_USER = "/mobilews/logonUser"


class MarketingMessageEndpoint(Enum):

    MARKETING_MESSAGE = "/mobilews/marketingMessage/{pageNameAndSize}"
    MARKETING_MESSAGE_UNAUTH = "/mobilews/marketingMessageUnauth"


class MessageEndpoint(Enum):

    MESSAGE = "/mobilews/message"
    MESSAGE_ATTACHMENT = "/mobilews/message/attachment"
    MESSAGE_ATTACHMENT_ID = "/mobilews/message/attachment/{id}"
    MESSAGE_COUNT = "/mobilews/message/count"
    MESSAGE_DELETE = "/mobilews/message/delete"
    MESSAGE_EXPIRE = "/mobilews/message/expire"
    MESSAGE_RECIPIENT = "/mobilews/message/messageRecipient"
    MESSAGE_ID = "/mobilews/message/{id}"


class MicroDepositEndpoint(Enum):

    MICRODEPOSIT = "/mobilews/microdeposit"
    MICRODEPOSIT_ID = "/mobilews/microdeposit/{id}"


class NavEndpoint(Enum):

    NAV = "/mobilews/nav"


class OnlineActivityEndpoint(Enum):

    ONLINE_ACTIVITY_EXPORT = "/mobilews/onlineActivityExport/{id}"


class PDFEndpoint(Enum):

    PDF = "/mobilews/pdf"
    PDF_VALIDATE = "/mobilews/pdf/validate"


class PoliciesEndpoint(Enum):

    POLICIES = "/mobilews/policies"
    POLICIES_HYDRA = "/mobilews/policies/hydra"
    POLICIES_USER_ROLE = "/mobilews/policies/userrole"
    POLICIES_USERS = "/mobilews/policies/users"
    POLICIES_ID = "/mobilews/policies/{id}"
    POLICIES_APPROVE = "/mobilews/policies/{id}/approve"
    POLICY_FEATURES = "/mobilews/policyFeatures"
    POLICY_SET_COMPANY = "/mobilews/policySet/company"
    POLICY_SET_HYDRA = "/mobilews/policySet/hydra"
    POLICY_SET_USER = "/mobilews/policySet/user"
    POLICY_SET_ID = "/mobilews/policySet/{id}"


class PreLogonEndpoint(Enum):

    PRE_LOGON_USER = "/mobilews/preLogonUser"
    PRE_LOGON_USER_CLEAR_CACHE = "/mobilews/preLogonUser/clearCache"


class PushEndpoint(Enum):

    PUSH = "/mobilews/push"
    PUSH_TOKEN = "/mobilews/push/{qtwoToken}"


class RateAppEndpoint(Enum):

    RATE_DECLINE = "/mobilews/rateApp/decline"
    RATE = "/mobilews/rateApp/rate"


class RDCEndpoint(Enum):

    RDC = "/mobilews/rdc"
    RDC_NEW = "/mobilews/rdc/new"
    RDC_ID = "/mobilews/rdc/{id}"
    RDC_IMAGE = "/mobilews/rdc/{imageSide}"


class RegisterDeviceEndpoint(Enum):

    REGISTER_DEVICE = "/mobilews/registerDevice"
    REGISTER_NOTIFICATION = "/mobilews/registerNotificationRoom"


class ReportEndpoint(Enum):

    REPORT_LATEST = "/mobilews/report/latest"
    REPORT_PLAN = "/mobilews/report/plan"
    REPORT_PLAN_ID = "/mobilews/report/plan/{id}"
    REPORT_PLAN_ID_RUN = "/mobilews/report/plan/{id}/run"
    REPORT = "/mobilews/report/report"
    REPORT_ID = "/mobilews/report/report/{id}"
    REPORT_DETAIL_ID = "/mobilews/report/report/{id}/{detailId}"
    REPORT_TEMPLATE = "/mobilews/report/template"
    REPORT_TEMPLATE_ID = "/mobilews/report/template/{id}"


class SettingsEndpoint(Enum):

    ACCOUNT = "/mobilews/settings/account"
    CHALLENGE_CODE = "/mobilews/settings/challengeCode"
    CHANGE_LOGIN = "/mobilews/settings/changeLogin"
    ESTATEMENT = "/mobilews/settings/estatement"
    MFA = "/mobilews/settings/mfa"
    MFA_FORM = "/mobilews/settings/mfa/form"
    MFA_ID = "/mobilews/settings/mfa/{id}"
    MOBILE_AUTH = "/mobilews/settings/mobileAuth"
    PASSWORD_POLICY = "/mobilews/settings/passwordPolicy"
    SECURITY_ALERT = "/mobilews/settings/securityAlert"
    TEXT_BANKING = "/mobilews/settings/textbanking"


class SSOEndpoint(Enum):

    SSO_BILL_PAY = "/mobilews/sso/billpay"
    SSO_BILL_PAY_ID = "/mobilews/sso/billpay/{id}"
    SSO_GENERIC_ID = "/mobilews/sso/generic/{id}/{accountId}"
    SSO_VENDOR_ID = "/mobilews/sso/vendor/{id}"


class ThemeEndpoint(Enum):

    THEME = "/mobilews/theme"


class TransactionEndpoint(Enum):

    TRANSACTION_APPROVE_MULTI_RECURRING = "/mobilews/transaction/approveMultiRecurring"
    TRANSACTION_MULTI = "/mobilews/transaction/multi"
    TRANSACTION_ID = "/mobilews/transaction/{id}"
    TRANSACTION_INQUIRY_LINK = "/mobilews/transaction/{id}/inquiryLink"
    TRANSACTION_NOTIFY = "/mobilews/transaction/{transactionId}/notify"
    TRANSACTION_NOTIFY_BATCH = "/mobilews/transaction/{transactionId}/notifyBatch"
    TRANSACTION_TYPE = "/mobilews/transaction/{type}"
    TRANSACTION_FORM = "/mobilews/transactionform/{type}"
    TRANSACTIONS = "/mobilews/transactions"
    TRANSACTIONS_COLUMNS = "/mobilews/transactions/columns"
    TRANSACTIONS_PENDING = "/mobilews/transactions/pending"
    TRANSACTIONS_PENDING_ONLY_DUAL = "/mobilews/transactions/pending/{onlyDual}"
    TRANSACTIONS_RECURRING = "/mobilews/transactions/recurring"
    TRANSACTIONS_RECURRING_ID = "/mobilews/transactions/recurring/{id}"


class UserEndpoint(Enum):

    USER = "/mobilews/user"
    USER_ROLE_ID = "/mobilews/user/role/{id}"
    USER_ROLE_DECIDE = "/mobilews/user/role/{id}/decide"
    USER_STATUS_ID = "/mobilews/user/status/{id}"
    USER_STATUS_DECIDE = "/mobilews/user/status/{id}/decide"
    USER_ID = "/mobilews/user/{id}"
    USER_PROFILE = "/mobilews/userProfile"
    USER_PROFILE_DECIDE_ID = "/mobilews/userProfile/decide/{id}"
    USER_PROFILE_FORM = "/mobilews/userProfile/form"
    USER_PROFILE_ID = "/mobilews/userProfile/{id}"
    USER_AGENT = "/mobilews/useragent"


class ConfigEndpoint(Enum):

    UUX_CONFIGURATION = "/mobilews/uuxConfiguration"


class V2Endpoint(Enum):

    COMMERCIAL_TAX_PAYMENT = "/mobilews/v2/commercial/taxpayment"
    COMMERCIAL_TAX_PAYMENT_ID = "/mobilews/v2/commercial/taxpayment/{id}"
