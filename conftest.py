from collections import namedtuple
from datetime import datetime
import pytest
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def prepare_user():
    now = datetime.now()
    data = now.strftime("%Y_%m_%d_%H_%M_%S")
    login = f'login_{data}'
    email = f'login_{data}@mail.ru'
    password = '12345678'
    user = namedtuple('User', 'login, email, password')
    return user(login=login, email=email, password=password)
