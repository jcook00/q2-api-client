from enum import Enum


class EnumEndpoint(Enum):

    CURRENCY = "/v3/currency"
    PRODUCT = "/v3/product"


class StatusEndpoint(Enum):

    ACTION_STATUS = "/v3/actionStatus"
    RDC_STATUS = "/v3/rdcStatus"
    RECURRING_ACTION_STATUS = "/v3/recurringActionStatus"


class TypeEndpoint(Enum):

    ACTION_TYPE = "/v3/actionType"
    IMAGE_TYPE = "/v3/imageType"
    PRODUCT_TYPE = "/v3/productType"


class AccountEndpoint(Enum):

    RETRIEVE_ACCOUNTS = "/v3/account/retrieve"
    RETRIEVE_ACCOUNT = "/v3/account/{id}/retrieve"
    UPDATE_ACCOUNT = "/v3/account/{id}/update"


class ActionEndpoint(Enum):

    RETRIEVE_ACTIONS = "/v3/action/retrieve"
    RETRIEVE_ACTION = "/v3/action/{id}/retrieve"


class AuthenticationEndpoint(Enum):

    KEEP_ALIVE = "/v3/keepalive"
    LOGIN = "/v3/login"
    LOGOFF = "/v3/logoff"
    MFA_LOGIN = "/v3/mfaLogin"
    PRE_LOGIN = "/v3/preLogin"
    REGISTER_DEVICE = "/v3/registerDevice"
    RETRIEVE_STATUS = "/v3/retrieveStatus"
    VALIDATE_MFA = "/v3/validateMfa"


class ElementEndpoint(Enum):

    RETRIEVE_ELEMENTS = "/v3/element/retrieve"
    RETRIEVE_ELEMENT = "/v3/element/{id}/retrieve"


class FileEndpoint(Enum):

    RETRIEVE_FILE = "/v3/file/{id}/retrieve"


class FundsTransferEndpoint(Enum):

    CREATE_FUNDS_TRANSFER = "/v3/fundsTransfer/create"
    FUNDS_TRANSFER_PERMISSION = "/v3/fundsTransfer/permission"
    RETRIEVE_FUNDS_TRANSFERS = "/v3/fundsTransfer/retrieve"
    AUTHORIZE_FUNDS_TRANSFER = "/v3/fundsTransfer/{id}/authorize"
    CANCEL_FUNDS_TRANSFER = "/v3/fundsTransfer/{id}/cancel"
    RETRIEVE_FUNDS_TRANSFER = "/v3/fundsTransfer/{id}/retrieve"


class ImageEndpoint(Enum):

    RETRIEVE_IMAGE = "/v3/image/{id}/retrieve"


class MessageEndpoint(Enum):

    CREATE_MESSAGE = "/v3/message/create"
    RETRIEVE_MESSAGES = "/v3/message/retrieve"
    RETRIEVE_UNREAD_MESSAGE_COUNT = "/v3/message/retrieveUnreadCount"
    RETRIEVE_MESSAGE = "/v3/message/{id}/retrieve"
    UPDATE_MESSAGE = "/v3/message/{id}/update"


class MessageRecipientGroupEndpoint(Enum):

    RETRIEVE_MESSAGE_RECIPIENT_GROUP = "/v3/messageRecipientGroup/retrieve"


class PasswordEndpoint(Enum):

    PASSWORD_PERMISSION = "/v3/password/permission"
    UPDATE_PASSWORD = "/v3/password/update"


class PFMAccountEndpoint(Enum):

    PFM_ACCOUNT_PERMISSION = "/v3/pfmAccount/permission"
    RETRIEVE_PFM_ACCOUNTS = "/v3/pfmAccount/retrieve"
    RETRIEVE_PFM_ACCOUNT = "/v3/pfmAccount/{id}/retrieve"


class RDCEndpoint(Enum):

    CREATE_RDC = "/v3/rdc/create"
    RDC_PERMISSIONS = "/v3/rdc/permission"
    RETRIEVE_RDCS = "/v3/rdc/retrieve"
    RETRIEVE_RDC = "/v3/rdc/{id}/retrieve"


class RecurringActionEndpoint(Enum):

    RETRIEVE_RECURRING_ACTIONS = "/v3/recurringAction/retrieve"


class RecurringFundsTransferEndpoint(Enum):

    CREATE_RECURRING_FUNDS_TRANSFER = "/v3/recurringFundsTransfer/create"
    RECURRING_FUNDS_TRANSFER_PERMISSIONS = "/v3/recurringFundsTransfer/permission"
    RETRIEVE_RECURRING_FUNDS_TRANSFERS = "/v3/recurringFundsTransfer/retrieve"
    AUTHORIZE_RECURRING_FUNDS_TRANSFER = "/v3/recurringFundsTransfer/{id}/authorize"
    CANCEL_RECURRING_FUNDS_TRANSFER = "/v3/recurringFundsTransfer/{id}/cancel"
    RETRIEVE_RECURRING_FUNDS_TRANSFER = "/v3/recurringFundsTransfer/{id}/retrieve"


class StatementEndpoint(Enum):

    RETRIEVE_STATEMENTS = "/v3/statement/retrieve"
    GENERATE_STATEMENT_URL = "/v3/statement/{id}/generateUrl"
    STATEMENT_KEY = "/v3/statement/{key}"


class TACEndpoint(Enum):

    RETRIEVE_TAC = "/v3/tac/retrieve"
    GENERATE_TAC = "/v3/tac/{id}/generate"


class TransactionEndpoint(Enum):

    RETRIEVE_TRANSACTIONS = "/v3/transaction/retrieve"
    RETRIEVE_TRANSACTION = "/v3/transaction/{id}/retrieve"


class TransactionDetailEndpoint(Enum):

    RETRIEVE_TRANSACTION_DETAILS = "/v3/transactionDetail/retrieve"


class UserEndpoint(Enum):

    RETRIEVE_USERS = "/v3/user/retrieve"
    RETRIEVE_SELF = "/v3/user/retrieveSelf"
    UPDATE_SELF = "/v3/user/updateSelf"
