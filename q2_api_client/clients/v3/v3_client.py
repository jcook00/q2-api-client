from q2_api_client.clients.v3.account_client import AccountClient
from q2_api_client.clients.v3.action_client import ActionClient
from q2_api_client.clients.v3.authentication_client import AuthenticationClient
from q2_api_client.clients.v3.element_client import ElementClient
from q2_api_client.clients.v3.enum_client import EnumClient
from q2_api_client.clients.v3.file_client import FileClient
from q2_api_client.clients.v3.funds_transfer_client import FundsTransferClient
from q2_api_client.clients.v3.image_client import ImageClient
from q2_api_client.clients.v3.message_client import MessageClient
from q2_api_client.clients.v3.message_recipient_group_client import MessageRecipientGroupClient
from q2_api_client.clients.v3.password_client import PasswordClient
from q2_api_client.clients.v3.pfm_account_client import PFMAccountClient
from q2_api_client.clients.v3.rdc_client import RDCClient
from q2_api_client.clients.v3.recurring_action_client import RecurringActionClient
from q2_api_client.clients.v3.recurring_funds_transfer_client import RecurringFundsTransferClient
from q2_api_client.clients.v3.statement_client import StatementClient
from q2_api_client.clients.v3.status_client import StatusClient
from q2_api_client.clients.v3.tac_client import TACClient
from q2_api_client.clients.v3.transaction_client import TransactionClient
from q2_api_client.clients.v3.transaction_detail_client import TransactionDetailClient
from q2_api_client.clients.v3.type_client import TypeClient
from q2_api_client.clients.v3.user_client import UserClient


class V3Client:

    def __init__(self, **kwargs):
        self._enum = EnumClient(**kwargs)
        kwargs['q2token'] = self._enum.get_header('q2token')
        self._status = StatusClient(**kwargs)
        self._type = TypeClient(**kwargs)
        self._account = AccountClient(**kwargs)
        self._action = ActionClient(**kwargs)
        self._authentication = AuthenticationClient(**kwargs)
        self._element = ElementClient(**kwargs)
        self._file = FileClient(**kwargs)
        self._funds_transfer = FundsTransferClient(**kwargs)
        self._image = ImageClient(**kwargs)
        self._message = MessageClient(**kwargs)
        self._message_recipient_group = MessageRecipientGroupClient(**kwargs)
        self._password = PasswordClient(**kwargs)
        self._pfm_account = PFMAccountClient(**kwargs)
        self._rdc = RDCClient(**kwargs)
        self._recurring_action = RecurringActionClient(**kwargs)
        self._recurring_funds_transfer = RecurringFundsTransferClient(**kwargs)
        self._statement = StatementClient(**kwargs)
        self._tac = TACClient(**kwargs)
        self._transaction = TransactionClient(**kwargs)
        self._transaction_detail = TransactionDetailClient(**kwargs)
        self._user = UserClient(**kwargs)

    @property
    def enum(self):
        return self._enum

    @property
    def status(self):
        return self._status

    @property
    def type(self):
        return self._type

    @property
    def account(self):
        return self._account

    @property
    def action(self):
        return self._action

    @property
    def authentication(self):
        return self._authentication

    @property
    def element(self):
        return self._element

    @property
    def file(self):
        return self._file

    @property
    def funds_transfer(self):
        return self._funds_transfer

    @property
    def image(self):
        return self._image

    @property
    def message(self):
        return self._message

    @property
    def message_recipient_group(self):
        return self._message_recipient_group

    @property
    def password(self):
        return self._password

    @property
    def pfm_account(self):
        return self._pfm_account

    @property
    def rdc(self):
        return self._rdc

    @property
    def recurring_action(self):
        return self._recurring_action

    @property
    def recurring_funds_transfer(self):
        return self._recurring_funds_transfer

    @property
    def statement(self):
        return self._statement

    @property
    def tac(self):
        return self._tac

    @property
    def transaction(self):
        return self._transaction

    @property
    def transaction_detail(self):
        return self._transaction_detail

    @property
    def user(self):
        return self._user
