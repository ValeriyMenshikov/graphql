import structlog
import schema
from graphql_client.client import GraphQLClient
from schema import RegistrationInput, schema

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_register_account():
    client = GraphQLClient(
        host='http://localhost:5051/graphql',
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
