from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from schema import PagingQueryInput, Query, AccountsResponse, schema
from graphql_client.client import GraphQLClient
import schema
import pprint


def test_accounts():
    client = GraphQLClient(
        service_name='http://localhost:5051/',
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
    response = client.request(query=query)
    pprint.pprint(response)
