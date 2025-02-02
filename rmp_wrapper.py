from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from constants import *

class RMPWrapper:
    def __init__(self, endpoint_url=ENDPOINT, auth_header=AUTH):
        self.transport = AIOHTTPTransport(
            url=endpoint_url,
            headers={
                "Content-Type": "application/json",
                "Authorization": auth_header,
            }
        )
        self.client = Client(
            transport=self.transport,
            fetch_schema_from_transport=True
        )

    def execute_query(self, query, variables):
        try:
            return self.client.execute(query, variable_values=variables)
        except Exception as e:
            print("Execution failed:", e)
