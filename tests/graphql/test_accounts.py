from modules.graphql.account_api.schema import PagingQueryInput


def test_accounts(logic):
    paging = PagingQueryInput()
    logic.provider.graphql.account_api.accounts(paging=paging, with_inactive=True)
