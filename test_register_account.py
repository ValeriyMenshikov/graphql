from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

import schema
from schema import Mutation, RegistrationInput, AccountRegisterResponse
import pprint


def test_register_account():
    url = 'http://localhost:5051/graphql'
    mutation = Operation(schema.Mutation, 'registerAccount')
    mutation_query = RegistrationInput(
        email="valeriy_menshikov1@mail.ru",
        login="valeriy_menshikov1",
        password="valeriy_menshikov1"
    )
    mutation.register_account(registration=mutation_query)
    print(mutation)
    endpoint = HTTPEndpoint(url)
    data = endpoint(mutation)
    pprint.pprint(data)
