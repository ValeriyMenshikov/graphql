from account_api.schema import RegistrationInput, UUID


def test_register_account(mailhog_api, account_api):
    email = "valeriy_menshikov2@mail.ru"
    login = "valeriy_menshikov2"
    password = "valeriy_menshikov2"
    registration = RegistrationInput(
        email=email,
        login=login,
        password=password,
    )
    account_api.register_account(registration=registration)
    activation_token = mailhog_api.get_token_from_last_email()
    account_api.activate_account(activation_token=UUID(activation_token))
