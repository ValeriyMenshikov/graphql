from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from schema import PagingQueryInput, Query, AccountsResponse
import schema
import pprint


def test_accounts():
    url = 'http://localhost:5051/graphql'
    paging = PagingQueryInput(
        skip=0,
        number=0,
        size=10
    )
    query = Operation(schema.Query, 'accounts')
    query.accounts(paging=paging, with_inactive=True)
    # query.accounts.__fields__(users=True, paging=True)
    query.accounts.users.__fields__('login', 'email', 'is_authenticated')
    print(query)

    endpoint = HTTPEndpoint(url)
    data = endpoint(query)
    pprint.pprint(data)
