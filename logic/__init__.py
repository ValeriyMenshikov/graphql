from functools import cached_property


class _LogicProvider:
    @cached_property
    def account_api(self):
        from logic.account_api import AccountConnector
        return AccountConnector()


logic_provider = _LogicProvider()
