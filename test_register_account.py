from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

import schema
from graphql_client.client import GraphQLClient
from schema import Mutation, RegistrationInput, AccountRegisterResponse, schema
import pprint


def test_register_account():
    client = GraphQLClient(
        service_name='http://localhost:5051/',
        schema=schema
    )
    mutation = client.mutation('registerAccount')
    mutation_query = RegistrationInput(
        email="valeriy_menshikov2@mail.ru",
        login="valeriy_menshikov2",
        password="valeriy_menshikov2"
    )
    mutation.register_account(registration=mutation_query)
    response = client.request(mutation)
    pprint.pprint(response)
