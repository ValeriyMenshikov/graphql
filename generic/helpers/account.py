from modules.graphql.account_api.schema import UpdateUserInput, RegistrationInput
from modules import modules_provider as mp


class AccountHelper:
    def __init__(self):
        self.account = mp.graphql.account_api
        self.mailhog_api = mp.http.mailhog_api

    def register_account(self, login, email, password):
        registration = RegistrationInput(
            login=login,
            email=email,
            password=password
        )
        self.account.register_account(
            registration=registration
        )
        activation_token = self.mailhog_api.get_token_from_last_email()
        response = self.account.activate_account(
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
        response = self.account.update_account(
            access_token=access_token,
            user_data=user_data
        )
        return response
