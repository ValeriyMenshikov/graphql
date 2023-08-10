from sgqlc.endpoint.http import HTTPEndpoint
import pprint


def test_accounts():
    url = 'http://localhost:5051/graphql'

    query = '''
    query($paging: PagingQueryInput) {
      accounts(withInactive: true, paging: $paging) {
          users {
              login,
              email,
              location
              isAuthenticated
          },
          paging {
              currentPage,
              totalPagesCount,
              totalEntitiesCount
          }
      }
    }
    '''
    variables = {
        "paging": {
            "size": 10,
            "skip": 0
        }
    }

    endpoint = HTTPEndpoint(url)
    data = endpoint(query, variables)
    pprint.pprint(data)
