import structlog
from client import GraphQLAccountApi

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_register_account():
    client = GraphQLAccountApi(
        host='http://5.63.153.31:5051/graphql',
    )

    email = "valeriy_menshikov2@mail.ru"
    login = "valeriy_menshikov2"
    password = "valeriy_menshikov2"

    client.register_account(
        email=email,
        login=login,
        password=password,
    )
