from sgqlc.endpoint.http import HTTPEndpoint
import pprint


def test_register_account():
    url = 'http://localhost:5051/graphql'
    mutation = '''
    mutation registerAccount($registration: RegistrationInput) {
      registerAccount(registration: $registration) {
          id,
          login
      }
    }
        '''
    variables = {
        "registration": {
            "email": "valeriy_menshikov@mail.ru",
            "login": "valeriy_menshikov",
            "password": "valeriy_menshikov"
        }
    }

    endpoint = HTTPEndpoint(url)
    data = endpoint(mutation, variables)
    pprint.pprint(data)
