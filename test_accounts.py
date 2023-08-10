from schema import PagingQueryInput, schema
from graphql_client.client import GraphQLClient
import schema
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_accounts():
    client = GraphQLClient(
        host='http://localhost:5051/graphql',
        schema=schema
    )

    paging = PagingQueryInput(
        skip=0,
        number=0,
        size=10
    )

    query = client.query(name='accounts')
    query.accounts(paging=paging, with_inactive=True)
    # query.accounts.__fields__(users=True, paging=True)
    query.accounts.users.__fields__('login', 'email', 'is_authenticated')
    client.request(query=query)
