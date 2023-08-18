from functools import cached_property


class AccountConnector:
    @cached_property
    def graphql(self):
        from logic.account_api.graphql import AccountGraphQLConnector
        return AccountGraphQLConnector()
