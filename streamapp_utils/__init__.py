from streamlit import connection
from streamapp_utils.snow_class import SnowConnection
from streamapp_utils.authenticator import Auth
from streamapp_utils.enviroment_selector import EnvironmentSelector
from streamapp_utils.report_generator import ReportGenerator
from streamapp_utils.roles import Roles
from streamapp_utils.cards import Card
from streamapp_utils.validators import BaseValidator
from streamapp_utils.requests import BaseRequest
from streamapp_utils import utils


class Conn:

    @property
    def connection(cls):
        return connection('snow', type=SnowConnection)

    @property
    def query(cls):
        return connection('snow', type=SnowConnection).query

    @property
    def query_async(cls):
        return connection('snow', type=SnowConnection).query_async

    @property
    def get_async_results(cls):
        return connection('snow', type=SnowConnection).get_async_results


conn = Conn()
login = Auth.login
setattr(BaseValidator, 'conn', conn)

__all__ = [
    'EnvironmentSelector',
    'ReportGenerator',
    'Roles',
    'Card',
    'BaseRequest',
    'utils',
    'BaseValidator'
]
