from streamlit import connection
from streamapp_utils.snow_class import SnowConnection
from streamapp_utils.authenticator import Auth
from streamapp_utils.enviroment_selector import EnviromentSelector
from streamapp_utils.report_generator import ReportGenerator
from streamapp_utils.roles import Roles
from streamapp_utils.cards import Card


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

__all__ = [
    'EnviromentSelector',
    'ReportGenerator',
    'Roles',
    'Card'
]
