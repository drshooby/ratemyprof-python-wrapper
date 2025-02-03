import json

from queries import *
from rmp_wrapper import RMPWrapper

rmp = RMPWrapper()

SEARCH_SCHOOL_VARIABLES = build_school_search_query("School name")

SEARCH_PROF_VARIABLES = build_teacher_search_query("Prof name (more specific the better)", "School ID, not legacyId")

GET_RATINGS_VARIABLES = build_rating_query("Prof ID from previous query, not legacyId")


if __name__ == "__main__":
    response = rmp.execute_query(NEW_SEARCH_SCHOOLS_QUERY, SEARCH_SCHOOL_VARIABLES)
    print(json.dumps(response, indent=4))