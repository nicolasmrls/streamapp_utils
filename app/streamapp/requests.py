from streamlit import session_state, secrets, toast
from requests import get, post, put, patch
from requests.exceptions import MissingSchema
from pydantic._internal._model_construction import ModelMetaclass
from typing import Optional
from itertools import cycle


class BaseRequest:
    methods = {
        'get': get,
        'post': post,
        'put': put,
        'patch': patch
    }
    headers = {
        'Content-Type': 'application/json'
    }

    @staticmethod
    def __get_url(request_type: str, include: str = '',
                  use_environment: bool = True):
        if use_environment:
            microservice = session_state.get('environment_url', '')
        else:
            microservice = ''
        url = secrets.REQUESTS.get(request_type).get('url')
        return microservice + url + include

    @staticmethod
    def __method(request_type: str):
        return secrets.REQUESTS.get(request_type).get('method')

    @classmethod
    def __send_json(cls, body: ModelMetaclass, url: str, request_type: str):
        response = cls.methods.get(cls.__method(request_type), 'get')(
            url=url,
            headers=cls.headers,
            data=body.model_dump_json()
        )
        return response

    @classmethod
    def __send_url(cls, url: str, request_type: str):
        response = cls.methods.get(cls.__method(request_type), 'get')(
            url=url
        )
        return response

    @classmethod
    def send(cls, request_type: str, body: Optional[dict] = None,
             include_in_url: str = '', is_json: bool = False,
             message: str = '', use_environment: bool = True):
        try:
            url = cls.__get_url(
                request_type=request_type,
                include=include_in_url,
                use_environment=use_environment
            )
            if is_json:
                response = cls.__send_json(
                    body=body,
                    request_type=request_type,
                    url=url
                )
            else:
                response = cls.__send_url(
                    request_type=request_type,
                    url=url
                )

            if response.status_code == 200:
                toast('Success ' + message, icon='✅')
            else:
                toast(f'Error {response.status_code} ' + message, icon='⛔')
            return response.content
        except MissingSchema:
            toast('Invalid host', icon='❌')
            return
        except AttributeError:
            toast('No request found', icon='❌')
            return
        except Exception as e:
            toast(e, icon='❌')
            return

    @classmethod
    def send_multiple(cls, request_type: str, bodies: list = [None],
                      include_in_url: list[str] = [''], is_json: bool = False,
                      use_environment: bool = True):
        try:
            assert abs(len(include_in_url) - len(bodies)) \
                == (max(len(include_in_url), len(bodies)) - 1), \
                'Invalid convination in bodies and url`s endings'
        except AssertionError as e:
            return [e]

        if len(bodies) < len(include_in_url):
            req = zip(cycle(bodies), include_in_url)
        elif len(bodies) > len(include_in_url):
            req = zip(bodies, cycle(include_in_url))
        else:
            req = zip(bodies, include_in_url)

        response = []
        for n, request in enumerate(req, 1):
            response.append(
                cls.send(
                    request_type=request_type,
                    body=request[0],
                    include_in_url=request[1],
                    is_json=is_json,
                    message=str(n),
                    use_environment=use_environment
                )
            )
        return response
