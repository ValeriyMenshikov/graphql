from client import GraphQLAccountApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_accounts():
    client = GraphQLAccountApi(
        host='http://localhost:5051/graphql',
    )
    client.accounts()
