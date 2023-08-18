from modules import modules_provider as mp
from modules.graphql.account_api.schema import *


class RegisterAccountLogic:
    def __init__(self):
        self._register_account = mp.graphql.account_api.register_account
        self._get_token = mp.http.mailhog_api.get_token_from_last_email
        self._activate_account = mp.graphql.account_api.activate_account

    def register_account(self, login, email, password):
        registration = RegistrationInput(
            login=login,
            email=email,
            password=password
        )
        response = self._register_account(registration=registration)
        token = self._get_token()
        response = self._activate_account(activation_token=UUID(token))
        return response
