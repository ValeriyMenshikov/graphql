from client import GraphQLAccountApi
import structlog

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


def test_accounts():
    client = GraphQLAccountApi(
        host='http://5.63.153.31:5051/graphql',
    )
    client.accounts()
