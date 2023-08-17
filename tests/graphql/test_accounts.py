from modules.account_api.schema import PagingQueryInput


def test_accounts(account_api):
    paging = PagingQueryInput()

    account_api.accounts(paging=paging, with_inactive=True)
