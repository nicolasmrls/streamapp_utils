from streamlit import connection
from base.snow_class import SnowConnection
from base.authenticator import Auth
from base.enviroment_selector import EnviromentSelector
from base.report_generator import ReportGenerator
from base.roles import Roles
from base.cards import Card


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
