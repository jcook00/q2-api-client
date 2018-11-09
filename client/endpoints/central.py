from enum import Enum


class CSREndpoint(Enum):

    CONFIG = "/central/csr/config/{name}"
    CONFIG_PREFIXED = "/central/csr/config/{name}/{prefixNameWithLoginDot}"
    DASHBOARD_ACTIVITY = "/central/csr/dashboardActivity"
    NAV = "/central/csr/nav"
    PROPERTIES = "/central/csr/properties"


class GamEndpoint(Enum):

    RIGHTS = "/central/gam/rights"
    TEAM = "/central/gam/team"
    TEAM_ID = "/central/gam/team/{team_id}"
    USER_ID = "/central/gam/user/{user_id}"


class LookupEndpoint(Enum):

    CUSTOMER_ID = "/central/lookup/customer/{customerId}"
    SEARCH = "/central/lookup/search"
    SORT_FIELDS = "/central/lookup/sort-fields"
    USER_ID = "/central/lookup/user/{userId}"
    USER_LOGON = "/central/lookup/userlogon/{userlogonId}"
