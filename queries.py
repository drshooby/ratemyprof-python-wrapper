from gql import gql

SCHOOL_SEARCH_QUERY = gql(
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

PROF_SEARCH_QUERY = gql(
"""
query NewSearchTeachersQuery(
$query: TeacherSearchQuery!
$count: Int!
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
"""
)

RATINGS_SEARCH_QUERY = gql(
"""
query TeacherRatingsPageQuery($id: ID!) {
  node(id: $id) {
    ... on Teacher {
      id
      legacyId
      firstName
      lastName
      department
      avgRating
      avgDifficulty
      wouldTakeAgainPercent
      ratingsDistribution {
        total
        r1
        r2
        r3
        r4
        r5
      }
    }
  }
}
"""
)