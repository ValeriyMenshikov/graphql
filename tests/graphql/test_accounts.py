from modules.graphql.account_api.schema import PagingQueryInput


def test_accounts(module_provider):
    paging = PagingQueryInput()

    module_provider.graphql.account_api.accounts(paging=paging, with_inactive=True)
