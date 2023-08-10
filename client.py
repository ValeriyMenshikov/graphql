from commons.graphql_client.client import GraphQLClient
from schema import (
    schema,
    Mutation,
    Query,
    RegistrationInput, PagingQueryInput
)


class GraphQLAccountApi:
    def __init__(self, host: str, headers: dict = None, disable_log: bool = False):
        self.host = host
        self.headers = headers
        self.disable_log = disable_log
        self.client = GraphQLClient(
            host=self.host,
            schema=schema,
            base_headers=self.headers,
            disable_log=self.disable_log
        )

    def register_account(self, email, login, password):
        mutation = self.client.mutation('registerAccount')
        mutation_query = RegistrationInput(
            email=email,
            login=login,
            password=password,
        )
        mutation.register_account(registration=mutation_query)
        response = self.client.request(mutation)
        return response

    def accounts(self, skip: int = 0, number: int = 0, size: int = 10):
        paging = PagingQueryInput(
            skip=skip,
            number=number,
            size=size
        )

        query = self.client.query(name='accounts')
        query.accounts(paging=paging, with_inactive=True)
        response = self.client.request(query=query)
        return response
