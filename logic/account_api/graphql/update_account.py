from modules import modules_provider as mp
from logic import logic_provider as lp
from modules.graphql.account_api.schema import *


class UpdateAccountLogic:
    def __init__(self):
        self._update_account = mp.graphql.account_api.update_account

    def update_account(self, access_token, **kwargs):
        user_data = UpdateUserInput()
        for param_name, value in kwargs.items():
            user_data.__setattr__(param_name, value)
        response = self._update_account(access_token=access_token, user_data=user_data)
        return response
