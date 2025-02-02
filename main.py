import json

from queries import *
from rmp_wrapper import RMPWrapper

rmp = RMPWrapper()

NEW_SEARCH_SCHOOLS_QUERY_VARIABLES = {
    "query": {
        "text": "", # School name here, more specific the better
    }
}

NEW_SEARCH_TEACHERS_QUERY_VARIABLES = {
    "query": {
        "text": "", # Prof name here
        "schoolID": "" # Use what you got from the query above (id not legacyId)
    },
    "count": 10, # Found this was a good number for search result count
}

TEACHER_RATINGS_PAGE_QUERY_VARIABLES = {
    "id": "" # Prof id here from query above
}

if __name__ == "__main__":
    response = rmp.execute_query(NEW_SEARCH_SCHOOLS_QUERY, NEW_SEARCH_SCHOOLS_QUERY_VARIABLES)
    print(json.dumps(response, indent=4))
    # response1 = rmp.execute_query(NEW_SEARCH_TEACHERS_QUERY, NEW_SEARCH_TEACHERS_QUERY_VARIABLES)
    # print(json.dumps(response1, indent=4))
    # response2 = rmp.execute_query(TEACHER_RATINGS_PAGE_QUERY, TEACHER_RATINGS_PAGE_QUERY_VARIABLES)
    # print(json.dumps(response2, indent=4))