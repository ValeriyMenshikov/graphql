from modules.graphql.account_api.schema import RegistrationInput, UUID, User, UserRole
from checkers.message_checkers import message_checker
from hamcrest import assert_that, has_properties, has_property, instance_of


def test_register_account(module_provider, prepare_user):
    email = prepare_user.email
    login = prepare_user.login
    password = prepare_user.password
    registration = RegistrationInput(
        email=email,
        login=login,
        password=password,
    )
    module_provider.graphql.account_api.register_account(registration=registration)
    activation_token = module_provider.http.mailhog_api.get_token_from_last_email()
    response = module_provider.graphql.account_api.activate_account(activation_token=UUID(activation_token))
    assert_that(response, has_property('resource', instance_of(User)))
    assert_that(response.resource, has_properties(
        {
            'login': login,
            'roles': [UserRole('GUEST'), UserRole('PLAYER')]
        }
    ))


def test_register_account_with_exists_login(module_provider):
    email = 'valeriy_menshikov5@mail.ru'
    login = 'valeriy_menshikov5'
    password = 'valeriy_menshikov'
    registration = RegistrationInput(
        email=email,
        login=login,
        password=password,
    )
    error_message = "Validation failed: \n -- Login: Taken Severity: Error\n -- Email: Taken Severity: Error"
    with message_checker(error_message=error_message):
        module_provider.graphql.account_api.register_account(registration=registration)
