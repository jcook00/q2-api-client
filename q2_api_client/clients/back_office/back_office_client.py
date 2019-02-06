from q2_api_client.clients.back_office.account_client import AccountClient
from q2_api_client.clients.back_office.authentication_client import AuthenticationClient
from q2_api_client.clients.back_office.branch_client import BranchClient
from q2_api_client.clients.back_office.csr_assist_client import CSRAssistClient
from q2_api_client.clients.back_office.custom_client import CustomClient
from q2_api_client.clients.back_office.customer_client import CustomerClient
from q2_api_client.clients.back_office.daily_action_cutoff_hour_client import DailyActionCutoffHourClient
from q2_api_client.clients.back_office.enum_client import EnumClient
from q2_api_client.clients.back_office.group_client import GroupClient
from q2_api_client.clients.back_office.holiday_action_cutoff_hour_client import HolidayActionCutoffHourClient
from q2_api_client.clients.back_office.status_client import StatusClient
from q2_api_client.clients.back_office.type_client import TypeClient
from q2_api_client.clients.back_office.user_client import UserClient
from q2_api_client.clients.back_office.user_login_client import UserLoginClient


class BackOfficeClient:

    def __init__(self, **kwargs):
        self._account = AccountClient(**kwargs)
        kwargs['q2token'] = self._account.get_header('q2token')
        self._authentication = AuthenticationClient(**kwargs)
        self._branch = BranchClient(**kwargs)
        self._csr_assist = CSRAssistClient(**kwargs)
        self._custom = CustomClient(**kwargs)
        self._customer = CustomerClient(**kwargs)
        self._daily_action_cutoff = DailyActionCutoffHourClient(**kwargs)
        self._enum = EnumClient(**kwargs)
        self._group = GroupClient(**kwargs)
        self._holiday_action_cutoff = HolidayActionCutoffHourClient(**kwargs)
        self._status = StatusClient(**kwargs)
        self._type = TypeClient(**kwargs)
        self._user = UserClient(**kwargs)
        self._user_login = UserLoginClient(**kwargs)

    @property
    def account(self):
        return self._account

    @property
    def authentication(self):
        return self._authentication

    @property
    def branch(self):
        return self._branch

    @property
    def csr_assist(self):
        return self._csr_assist

    @property
    def custom(self):
        return self._custom

    @property
    def customer(self):
        return self._customer

    @property
    def daily_action_cutoff(self):
        return self._daily_action_cutoff

    @property
    def enum(self):
        return self._enum

    @property
    def group(self):
        return self._group

    @property
    def holiday_action_cutoff(self):
        return self._holiday_action_cutoff

    @property
    def status(self):
        return self._status

    @property
    def type(self):
        return self._type

    @property
    def user(self):
        return self._user

    @property
    def user_login(self):
        return self._user_login
