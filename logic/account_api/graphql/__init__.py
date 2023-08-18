from functools import cached_property


class AccountGraphQLConnector:

    @cached_property
    def register_account(self):
        from logic.account_api.graphql.register_account import RegisterAccountLogic
        return RegisterAccountLogic()

    @cached_property
    def update_account(self):
        from logic.account_api.graphql.update_account import UpdateAccountLogic
        return UpdateAccountLogic()
