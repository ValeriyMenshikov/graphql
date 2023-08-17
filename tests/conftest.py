from collections import namedtuple
from datetime import datetime

import pytest
import structlog

from account_api.account_api import GraphQLAccountApiClient
from mailhog_api.mailhog_api import MailhogApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@pytest.fixture
def account_api():
    client = GraphQLAccountApiClient(
        host='http://5.63.153.31:5051/graphql',
    )
    return client


@pytest.fixture
def mailhog_api():
    client = MailhogApi(
        host='http://5.63.153.31:5025'
    )
    return client
