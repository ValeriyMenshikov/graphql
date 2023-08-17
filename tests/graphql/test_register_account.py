from modules.graphql.account_api.schema import RegistrationInput, UUID, User, UserRole
from generic.checkers.message_checkers import message_checker
from hamcrest import assert_that, has_properties, has_property, instance_of


def test_register_account(logic, prepare_user):
    email = prepare_user.email
    login = prepare_user.login
    password = prepare_user.password
    response = logic.account_helper.register_account(email=email, login=login, password=password)
    assert_that(response, has_property('resource', instance_of(User)))
    assert_that(response.resource, has_properties(
        {
            'login': login,
            'roles': [UserRole('GUEST'), UserRole('PLAYER')]
        }
    ))


def test_register_account_with_exists_login(logic):
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
        logic.provider.graphql.account_api.register_account(registration=registration)
