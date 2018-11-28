from q2_api_client.clients.mobile_ws.access_code_client import AccessCodeClient
from q2_api_client.clients.mobile_ws.account_client import AccountClient
from q2_api_client.clients.mobile_ws.account_export_client import AccountExportClient
from q2_api_client.clients.mobile_ws.account_history_client import AccountHistoryClient
from q2_api_client.clients.mobile_ws.account_pfm_client import AccountPFMClient
from q2_api_client.clients.mobile_ws.account_statement_client import AccountStatementClient
from q2_api_client.clients.mobile_ws.accounts_client import AccountsClient
from q2_api_client.clients.mobile_ws.adapter_client import AdapterClient
from q2_api_client.clients.mobile_ws.alerts_client import AlertsClient
from q2_api_client.clients.mobile_ws.antiphishing_client import AntiphishingClient
from q2_api_client.clients.mobile_ws.audit_client import AuditClient
from q2_api_client.clients.mobile_ws.bill_pay_client import BillPayClient
from q2_api_client.clients.mobile_ws.calendar_client import CalendarClient
from q2_api_client.clients.mobile_ws.commercial_client import CommercialClient
from q2_api_client.clients.mobile_ws.config_client import ConfigClient
from q2_api_client.clients.mobile_ws.csr_client import CSRClient
from q2_api_client.clients.mobile_ws.disclaimer_client import DisclaimerClient
from q2_api_client.clients.mobile_ws.edv_client import EDVClient
from q2_api_client.clients.mobile_ws.feeds_client import FeedsClient
from q2_api_client.clients.mobile_ws.fi_client import FIClient
from q2_api_client.clients.mobile_ws.form_client import FormClient
from q2_api_client.clients.mobile_ws.front_end_client import FrontEndClient
from q2_api_client.clients.mobile_ws.fsf_client import FSFClient
from q2_api_client.clients.mobile_ws.gam_client import GAMClient
from q2_api_client.clients.mobile_ws.keep_alive_client import KeepAliveClient
from q2_api_client.clients.mobile_ws.language_client import LanguageClient
from q2_api_client.clients.mobile_ws.locations_client import LocationsClient
from q2_api_client.clients.mobile_ws.login_client import LoginClient
from q2_api_client.clients.mobile_ws.marketing_message_client import MarketingMessageClient
from q2_api_client.clients.mobile_ws.message_client import MessageClient
from q2_api_client.clients.mobile_ws.micro_deposit_client import MicroDepositClient
from q2_api_client.clients.mobile_ws.nav_client import NavClient
from q2_api_client.clients.mobile_ws.online_activity_client import OnlineActivityClient
from q2_api_client.clients.mobile_ws.pdf_client import PDFClient
from q2_api_client.clients.mobile_ws.policies_client import PoliciesClient
from q2_api_client.clients.mobile_ws.pre_logon_client import PreLogonClient
from q2_api_client.clients.mobile_ws.push_client import PushClient
from q2_api_client.clients.mobile_ws.rate_app_client import RateAppClient
from q2_api_client.clients.mobile_ws.rdc_client import RDCClient
from q2_api_client.clients.mobile_ws.register_device_client import RegisterDeviceClient
from q2_api_client.clients.mobile_ws.report_client import ReportClient
from q2_api_client.clients.mobile_ws.security_client import SecurityClient
from q2_api_client.clients.mobile_ws.settings_client import SettingsClient
from q2_api_client.clients.mobile_ws.sso_client import SSOClient
from q2_api_client.clients.mobile_ws.theme_client import ThemeClient
from q2_api_client.clients.mobile_ws.transaction_client import TransactionClient
from q2_api_client.clients.mobile_ws.user_client import UserClient
from q2_api_client.clients.mobile_ws.v2_client import V2Client


class MobileWSClient:

    def __init__(self, **kwargs):
        self._access_code = AccessCodeClient(**kwargs)
        kwargs['q2token'] = self._access_code.get_header('q2token')
        self._account = AccountClient(**kwargs)
        self._account_export = AccountExportClient(**kwargs)
        self._account_history = AccountHistoryClient(**kwargs)
        self._account_pfm = AccountPFMClient(**kwargs)
        self._account_statement = AccountStatementClient(**kwargs)
        self._accounts = AccountsClient(**kwargs)
        self._adapter = AdapterClient(**kwargs)
        self._alerts = AlertsClient(**kwargs)
        self._antiphishing = AntiphishingClient(**kwargs)
        self._audit = AuditClient(**kwargs)
        self._bill_pay = BillPayClient(**kwargs)
        self._calendar = CalendarClient(**kwargs)
        self._security = SecurityClient(**kwargs)
        self._commercial = CommercialClient(**kwargs)
        self._csr = CSRClient(**kwargs)
        self._disclaimer = DisclaimerClient(**kwargs)
        self._edv = EDVClient(**kwargs)
        self._feeds = FeedsClient(**kwargs)
        self._fi = FIClient(**kwargs)
        self._form = FormClient(**kwargs)
        self._front_end = FrontEndClient(**kwargs)
        self._fsf = FSFClient(**kwargs)
        self._gam = GAMClient(**kwargs)
        self._keep_alive = KeepAliveClient(**kwargs)
        self._language = LanguageClient(**kwargs)
        self._locations = LocationsClient(**kwargs)
        self._login = LoginClient(**kwargs)
        self._marketing_message = MarketingMessageClient(**kwargs)
        self._message = MessageClient(**kwargs)
        self._micro_deposit = MicroDepositClient(**kwargs)
        self._nav = NavClient(**kwargs)
        self._online_activity = OnlineActivityClient(**kwargs)
        self._pdf = PDFClient(**kwargs)
        self._policies = PoliciesClient(**kwargs)
        self._pre_logon = PreLogonClient(**kwargs)
        self._push = PushClient(**kwargs)
        self._rate_app = RateAppClient(**kwargs)
        self._rdc = RDCClient(**kwargs)
        self._register_device = RegisterDeviceClient(**kwargs)
        self._report = ReportClient(**kwargs)
        self._settings = SettingsClient(**kwargs)
        self._sso = SSOClient(**kwargs)
        self._theme = ThemeClient(**kwargs)
        self._transaction = TransactionClient(**kwargs)
        self._user = UserClient(**kwargs)
        self._config = ConfigClient(**kwargs)
        self._v2 = V2Client(**kwargs)

    @property
    def access_code(self):
        return self._access_code

    @property
    def account(self):
        return self._account

    @property
    def account_export(self):
        return self._account_export

    @property
    def account_history(self):
        return self._account_history

    @property
    def account_pfm(self):
        return self._account_pfm

    @property
    def account_statement(self):
        return self._account_statement

    @property
    def accounts(self):
        return self._accounts

    @property
    def adapter(self):
        return self._adapter

    @property
    def alerts(self):
        return self._alerts

    @property
    def antiphishing(self):
        return self._antiphishing

    @property
    def audit(self):
        return self._audit

    @property
    def bill_pay(self):
        return self._bill_pay

    @property
    def calendar(self):
        return self._calendar

    @property
    def security(self):
        return self._security

    @property
    def commercial(self):
        return self._commercial

    @property
    def csr(self):
        return self._csr

    @property
    def disclaimer(self):
        return self._disclaimer

    @property
    def edv(self):
        return self._edv

    @property
    def feeds(self):
        return self._feeds

    @property
    def fi(self):
        return self._fi

    @property
    def form(self):
        return self._form

    @property
    def front_end(self):
        return self._front_end

    @property
    def fsf(self):
        return self._fsf

    @property
    def gam(self):
        return self._gam

    @property
    def keep_alive(self):
        return self._keep_alive

    @property
    def language(self):
        return self._language

    @property
    def locations(self):
        return self._locations

    @property
    def login(self):
        return self._login

    @property
    def marketing_message(self):
        return self._marketing_message

    @property
    def message(self):
        return self._message

    @property
    def micro_deposit(self):
        return self._micro_deposit

    @property
    def nav(self):
        return self._nav

    @property
    def online_activity(self):
        return self._online_activity

    @property
    def pdf(self):
        return self._pdf

    @property
    def policies(self):
        return self._policies

    @property
    def pre_logon(self):
        return self._pre_logon

    @property
    def push(self):
        return self._push

    @property
    def rate_app(self):
        return self._rate_app

    @property
    def rdc(self):
        return self._rdc

    @property
    def register_device(self):
        return self._register_device

    @property
    def report(self):
        return self._report

    @property
    def settings(self):
        return self._settings

    @property
    def sso(self):
        return self._sso

    @property
    def theme(self):
        return self._theme

    @property
    def transaction(self):
        return self._transaction

    @property
    def user(self):
        return self._user

    @property
    def config(self):
        return self._config

    @property
    def v2(self):
        return self._v2
