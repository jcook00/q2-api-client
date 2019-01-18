from enum import Enum


class AccountEndpoint(Enum):

    RETRIEVE_ACCOUNT = "/backoffice/v3/account/{id}/retrieve"


class AuthenticationEndpoint(Enum):

    LOGIN = "/backoffice/v3/login"


class BranchEndpoint(Enum):

    RETRIEVE_BRANCH = "/backoffice/v3/branch/retrieve"


class CSRAssistEndpoint(Enum):

    CREATE_CSR_ASSIST = "/backoffice/v3/csrAssist/create"


class CustomEndpoint(Enum):

    SEARCH_DELETED = "/custom/associate/searchDeleted"


class CustomerEndpoint(Enum):

    RETRIEVE_CUSTOMERS = "/backoffice/v3/customer/retrieve"
    RETRIEVE_CUSTOMER = "/backoffice/v3/customer/{id}/retrieve"


class DailyActionCutoffHourEndpoint(Enum):

    RETRIEVE_DAILY_ACTION_CUTOFFS = "/backoffice/v3/dailyActionCutoffHour/retrieve"
    RETRIEVE_DAILY_ACTION_CUTOFF = "/backoffice/v3/dailyActionCutoffHour/{id}/retrieve"
    UPDATE_DAILY_ACTION_CUTOFFS = "/backoffice/v3/dailyActionCutoffHour/{id}/update"


class TypeEndpoint(Enum):

    ACTION_TYPE = "/backoffice/v3/actionType"
    PHONE_TYPE = "/backoffice/v3/phoneType"


class StatusEndpoint(Enum):

    USER_LOGIN_STATUS = "/backoffice/v3/userLoginStatus"
    USER_STATUS = "/backoffice/v3/userStatus"


class EnumEndpoint(Enum):

    DAY_OF_THE_WEEK = "/backoffice/v3/dayOfTheWeek"


class GroupEndpoint(Enum):

    RETRIEVE_GROUP = "/backoffice/v3/group/{id}/retrieve"


class HolidayActionCutoffHourEndpoint(Enum):

    RETRIEVE_HOLIDAY_ACTION_CUTOFFS = "/backoffice/v3/holidayActionCutoffHour/retrieve"
    RETRIEVE_HOLIDAY_ACTION_CUTOFF = "/backoffice/v3/holidayActionCutoffHour/{id}/retrieve"


class UserEndpoint(Enum):

    RETRIEVE_USERS = "/backoffice/v3/user/retrieve"
    RETRIEVE_USER_ACCOUNT = "/backoffice/v3/user/{id}/account/retrieve"
    RETRIEVE_CSR_ASSIST_POLICY = "/backoffice/v3/user/{id}/csrAssistPolicy/retrieve"
    RETRIEVE_FEATURE_RIGHT = "/backoffice/v3/user/{id}/featureRight/retrieve"
    CREATE_PHONE = "/backoffice/v3/user/{id}/phone/create"
    RETRIEVE_PHONE = "/backoffice/v3/user/{id}/phone/retrieve"
    DELETE_PHONE = "/backoffice/v3/user/{id}/phone/{phoneId}/delete"
    UPDATE_PHONE = "/backoffice/v3/user/{id}/phone/{phoneId}/update"
    RESTORE_USER = "/backoffice/v3/user/{id}/restore"
    RETRIEVE_USER = "/backoffice/v3/user/{id}/retrieve"
    UPDATE_USER = "/backoffice/v3/user/{id}/update"
    RETRIEVE_USER_LOGIN = "/backoffice/v3/user/{id}/userLogin/retrieve"


class UserLoginEndpoint(Enum):

    RETRIEVE_USER_LOGINS = "/backoffice/v3/userLogin/retrieve"
    CHANGE_PASSWORD = "/backoffice/v3/userLogin/{id}/changePassword"
    PATCH_USER_LOGIN = "/backoffice/v3/userLogin/{id}/patch"
    RESET_DEVICE_REGISTRATION = "/backoffice/v3/userLogin/{id}/resetDeviceRegistration"
    RESTORE_USER_LOGIN = "/backoffice/v3/userLogin/{id}/restore"
    RETRIEVE_USER_LOGIN = "/backoffice/v3/userLogin/{id}/retrieve"
    UPDATE_USER_LOGIN = "/backoffice/v3/userLogin/{id}/update"
