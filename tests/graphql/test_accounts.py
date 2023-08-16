from account_api.account_api import GraphQLAccountApiClient
from account_api.schema import PagingQueryInput
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_accounts():
    client = GraphQLAccountApiClient(
        host='http://5.63.153.31:5051/graphql',
    )
    paging = PagingQueryInput()

    client.accounts(paging=paging, with_inactive=True)
