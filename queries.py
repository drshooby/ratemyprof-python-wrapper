from gql import gql

'''
This will help you find your School IDs for the Prof search for all of these use "id" not "legacyId", but leaving it just in case.
'''

NEW_SEARCH_SCHOOLS_QUERY = gql(
"""
query NewSearchSchoolsQuery(
$query: SchoolSearchQuery
) {
  newSearch {
    schools(query: $query) {
      edges {
        node {
          id
          legacyId
          name
          city
          state
        }
      }
    }
  }
}
"""
)

def build_school_search_query(school_text):
    return {"query": {
        "text": school_text,
    }}

'''
This will help you perform searches for Prof IDs based on what's passed into the variables
as they will be necessary for the ratings search.
'''

NEW_SEARCH_TEACHERS_QUERY = gql(
"""
query NewSearchTeachersQuery(
  $query: TeacherSearchQuery!
  $count: Int
) {
  newSearch {
    teachers(query: $query, first: $count) {
      didFallback
      edges {
        cursor
        node {
          id
          legacyId
          firstName
          lastName
          department
          departmentId
          school {
            legacyId
            name
            id
          }
        }
      }
    }
  }
}
""")

def build_teacher_search_query(prof_name_text, school_id_text, count=10):
    return {
        "query": {
            "text": prof_name_text,
            "schoolID": school_id_text
        },
        "count": count
    }

'''
This gets the rating information.
'''

TEACHER_RATINGS_PAGE_QUERY = gql(
"""
query TeacherRatingsPageQuery(
$id: ID!
) {
  node(id: $id) {
    ... on Teacher {
      id
      legacyId
      firstName
      lastName
      department
      ...StickyHeaderContent_teacher
      ...RatingDistributionWrapper_teacher
      ...TeacherInfo_teacher
      ...TeacherRatingTabs_teacher
    }
    id
  }
}

fragment StickyHeaderContent_teacher on Teacher {
  ...HeaderDescription_teacher
  ...HeaderRateButton_teacher
}

fragment RatingDistributionWrapper_teacher on Teacher {
  ratingsDistribution {
    total
    ...RatingDistributionChart_ratingsDistribution
  }
}

fragment TeacherInfo_teacher on Teacher {
  id
  lastName
  ...RatingValue_teacher
  ...NameTitle_teacher
  ...NameLink_teacher
  ...TeacherFeedback_teacher
  ...RateTeacherLink_teacher
}

fragment TeacherRatingTabs_teacher on Teacher {
  ...RatingsList_teacher
}

fragment RatingsList_teacher on Teacher {
  id
  legacyId
  lastName
  ...Rating_teacher
}

fragment Rating_teacher on Teacher {
  ...RatingFooter_teacher
}

fragment RateTeacherLink_teacher on Teacher {
  legacyId
}

fragment RatingFooter_teacher on Teacher {
  id
  legacyId
}

fragment RatingValue_teacher on Teacher {
  avgRating
}

fragment NameTitle_teacher on Teacher {
  id
  firstName
  lastName
  department
  ...TeacherDepartment_teacher
}

fragment NameLink_teacher on Teacher {
  id
  legacyId
  firstName
  lastName
}

fragment TeacherFeedback_teacher on Teacher {
  avgDifficulty
  wouldTakeAgainPercent
}

fragment TeacherDepartment_teacher on Teacher {
  department
}

fragment RatingDistributionChart_ratingsDistribution on ratingsDistribution {
  r1
  r2
  r3
  r4
  r5
}

fragment HeaderDescription_teacher on Teacher {
  id
  legacyId
  firstName
  lastName
  department
  ...TeacherTitles_teacher
  ...RateTeacherLink_teacher
}

fragment HeaderRateButton_teacher on Teacher {
  ...RateTeacherLink_teacher
}

fragment TeacherTitles_teacher on Teacher {
  department
}
""")

def build_rating_query(prof_id_text):
    return {
        "id": prof_id_text,
    }