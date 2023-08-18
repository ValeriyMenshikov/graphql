from logic import logic_provider as lp
from modules import modules_provider as mp
register_account = lp.account_api.graphql.register_account.register_account


class TestUpdateAccount:
    def __init__(self):
        self.register_account = lp.account_api.graphql.register_account.register_account
        self.update_account = lp.account_api.graphql.update_account.update_account

    def test_update_account(self, prepare_user):
        login = prepare_user.login
        email = prepare_user.email
        password = prepare_user.password
        self.register_account(login=login, email=email, password=password)

        mp.graphql.account_api.register_account()
        mp.http.mailhog_api.get_token_from_last_email()
        mp.graphql.account_api.activate_account()
        mp.graphql.account_api.login_account()


        self.update_account()
