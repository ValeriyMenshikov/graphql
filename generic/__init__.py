from functools import cached_property


class _LogicProvider:

    @cached_property
    def provider(self):
        from modules import modules_provider
        return modules_provider()

    @cached_property
    def account_api(self):
        from generic.helpers.account_api import AccountApiConnector
        return AccountApiConnector()

    @cached_property
    def mailhog_api(self):
        from generic.helpers.mailhog_api import MailHogApiConnector
        return MailHogApiConnector()


logic_provider = _LogicProvider()
