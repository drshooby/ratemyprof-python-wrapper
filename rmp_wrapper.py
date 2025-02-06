from gql import Client
from gql.transport.aiohttp import AIOHTTPTransport
from constants import *

class RMPWrapper:
    """Handles GraphQL requests to RateMyProfessors API."""

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
        """Executes a GraphQL query with the given variables."""
        try:
            return self.client.execute(query, variable_values=variables)
        except Exception as e:
            print("Execution failed:", e)


# URL builders
def build_school_link(legacy_id):
    """Generates a school profile link based on legacy ID."""
    return f"https://www.ratemyprofessors.com/school/{legacy_id}"


def build_rating_link(legacy_id):
    """Generates a professor rating profile link based on legacy ID."""
    return f"https://www.ratemyprofessors.com/professor/{legacy_id}"


# Query builders
def build_school_search_query(school_name):
    """Builds a search query for schools."""
    return {"query": {"text": school_name}}


def build_teacher_search_query(prof_name, school_id, count=10):
    """Builds a search query for professors at a given school."""
    return {"query": {"text": prof_name, "schoolID": school_id}, "count": count}


def build_rating_query(prof_id):
    """Builds a query to fetch ratings for a professor."""
    return {"id": prof_id}
