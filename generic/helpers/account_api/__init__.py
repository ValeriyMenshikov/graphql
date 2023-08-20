from functools import cached_property


class AccountApiConnector:
    @cached_property
    def graphql(self):
        from generic.helpers.account_api.graphql.account_helper import AccountApiGraphQLHelper
        return AccountApiGraphQLHelper()
