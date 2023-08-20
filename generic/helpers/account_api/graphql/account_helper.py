from modules.graphql.account_api.schema import UpdateUserInput, RegistrationInput
from modules import modules_provider as mp
from generic.helpers.mailhog_api.http.mailhog_helper import MailhogApiHttpHelper


class AccountApiGraphQLHelper:
    def __init__(self):
        self.account_api = mp.graphql.account_api
        self.mailhog_helper = MailhogApiHttpHelper()

    def register_account(self, login, email, password):
        registration = RegistrationInput(
            login=login,
            email=email,
            password=password
        )
        self.account_api.register_account(
            registration=registration
        )
        activation_token = self.mailhog_helper.get_token_from_last_email()
        response = self.account_api.activate_account(
            activation_token=activation_token
        )
        return response

    def update_account(
            self,
            access_token: str,
            **kwargs: dict[UpdateUserInput.__field_names__]
    ):
        """
        Обновить данные профиля текущего пользователя.
        :param access_token:
        :param kwargs:
        :return:
        """
        user_data = UpdateUserInput()
        for k, v in kwargs.items():
            user_data.__setattr__(k, v)
        response = self.account_api.update_account(
            access_token=access_token,
            user_data=user_data
        )
        return response
