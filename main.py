import json

from queries import *
from rmp_wrapper import *

rmp = RMPWrapper()

SEARCH_SCHOOL_VARIABLES = build_school_search_query("Your school")

SEARCH_PROF_VARIABLES = build_teacher_search_query("Prof name", "School id")

SEARCH_RATINGS_VARIABLES = build_rating_query("Prof id")

if __name__ == "__main__":
    # schools_response = rmp.execute_query(NEW_SEARCH_SCHOOLS_QUERY, SEARCH_SCHOOL_VARIABLES)
    # print(json.dumps(schools_response, indent=4))

    # profs_response = rmp.execute_query(NEW_SEARCH_TEACHERS_QUERY, SEARCH_PROF_VARIABLES)
    # print(json.dumps(profs_response, indent=4))

    # ratings_response = rmp.execute_query(RATINGS_SEARCH_QUERY, SEARCH_RATINGS_VARIABLES)
    # print(json.dumps(ratings_response, indent=4))
    pass