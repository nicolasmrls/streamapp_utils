from streamlit import connection
from streamapp.snow_class import SnowConnection
from streamapp.authenticator import Auth
from streamapp.enviroment_selector import EnvironmentSelector
from streamapp.report_generator import ReportGenerator
from streamapp.roles import Roles
from streamapp.cards import Card
from streamapp.validators import BaseValidator
from streamapp.requests import BaseRequest
from streamapp import utils


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
