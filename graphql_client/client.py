from typing import Any, Dict
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from sgqlc.types import Schema


class GraphQLClient:

    def __init__(
            self,
            schema: Schema,
            host: str,
            disable_log: bool = False,
            base_headers: dict = None
    ):
        self.schema = schema
        self.disable_log = disable_log
        self.host = host
        self._endpoint = HTTPEndpoint(self.host)

        if base_headers:
            self._endpoint.base_headers = base_headers

    def set_headers(self, headers: dict) -> None:
        self._endpoint.base_headers = headers

    def query(self, name: str) -> Operation:
        return Operation(self.schema.Query, name)

    def mutation(self, name: str) -> Operation:
        return Operation(self.schema.Mutation, name)

    def request(self, query: Operation) -> Dict[str, Any]:
        return self._endpoint(query)
