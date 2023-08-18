from functools import cached_property
from modules.graphql.account_api.account_api import GraphQLAccountApiClient
from config.config import settings


class GraphQLConnector:

    @cached_property
    def account_api(self) -> GraphQLAccountApiClient:
        return GraphQLAccountApiClient(host=settings.service.dm_api_account_graphql)
