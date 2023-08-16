from .schema import *
from commons.graphql_client.client import GraphQLClient


class GraphQLAccountApiClient:
    def __init__(self, host: str, headers: dict = None, disable_log: bool = False):
        self.host = host
        self.headers = headers
        self.disable_log = disable_log
        self.client = GraphQLClient(
            host=self.host,
            schema=schema,
            base_headers=self.headers,
            disable_log=self.disable_log
        )

    def account_current(self, access_token: String) -> dict:
        query_name = 'accountCurrent'
        query = self.client.query(name=query_name)
        query.account_current(
            access_token=access_token,
        )
        response = self.client.request(query=query)

        return response

    def accounts(self, paging: PagingQueryInput, with_inactive: Boolean) -> dict:
        query_name = 'accounts'
        query = self.client.query(name=query_name)
        query.accounts(
            paging=paging,
            with_inactive=with_inactive,
        )
        response = self.client.request(query=query)
        return response

    def register_account(self, registration: RegistrationInput) -> dict:
        query_name = 'registerAccount'
        mutation = self.client.mutation(name=query_name)
        mutation.register_account(
            registration=registration,
        )
        response = self.client.request(query=mutation)
        return response

    def activate_account(self, activation_token: UUID) -> dict:
        query_name = 'activateAccount'
        mutation = self.client.mutation(name=query_name)
        mutation.activate_account(
            activation_token=activation_token,
        )
        response = self.client.request(query=mutation)
        return response

    def change_account_email(self, change_email: ChangeEmailInput) -> dict:
        query_name = 'changeAccountEmail'
        mutation = self.client.mutation(name=query_name)
        mutation.change_account_email(
            change_email=change_email,
        )
        response = self.client.request(query=mutation)
        return response

    def reset_account_password(self, reset_password: ResetPasswordInput) -> dict:
        query_name = 'resetAccountPassword'
        mutation = self.client.mutation(name=query_name)
        mutation.reset_account_password(
            reset_password=reset_password,
        )
        response = self.client.request(query=mutation)
        return response

    def change_account_password(self, change_password: ChangePasswordInput) -> dict:
        query_name = 'changeAccountPassword'
        mutation = self.client.mutation(name=query_name)
        mutation.change_account_password(
            change_password=change_password,
        )
        response = self.client.request(query=mutation)
        return response

    def update_account(self, access_token: String, user_data: UpdateUserInput) -> dict:
        query_name = 'updateAccount'
        mutation = self.client.mutation(name=query_name)
        mutation.update_account(
            access_token=access_token,
            user_data=user_data,
        )
        response = self.client.request(query=mutation)
        return response

    def login_account(self, login: LoginCredentialsInput) -> dict:
        query_name = 'loginAccount'
        mutation = self.client.mutation(name=query_name)
        mutation.login_account(
            login=login,
        )
        response = self.client.request(query=mutation)
        return response

    def logout_account(self, access_token: String) -> dict:
        query_name = 'logoutAccount'
        mutation = self.client.mutation(name=query_name)
        mutation.logout_account(
            access_token=access_token,
        )
        response = self.client.request(query=mutation)
        return response

    def logout_all_account(self, access_token: String) -> dict:
        query_name = 'logoutAllAccount'
        mutation = self.client.mutation(name=query_name)
        mutation.logout_all_account(
            access_token=access_token,
        )
        response = self.client.request(query=mutation)
        return response
