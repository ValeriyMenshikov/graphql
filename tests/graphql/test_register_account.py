import structlog
from account_api.account_api import GraphQLAccountApiClient
from account_api.schema import RegistrationInput

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_register_account():
    client = GraphQLAccountApiClient(
        host='http://5.63.153.31:5051/graphql',
    )

    email = "valeriy_menshikov2@mail.ru"
    login = "valeriy_menshikov2"
    password = "valeriy_menshikov2"
    registration = RegistrationInput(
        email=email,
        login=login,
        password=password,
    )
    client.register_account(registration=registration)
