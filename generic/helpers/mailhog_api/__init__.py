from functools import cached_property


class MailHogApiConnector:
    @cached_property
    def graphql(self):
        from generic.helpers.mailhog_api.http.mailhog_helper import MailhogApiHttpHelper
        return MailhogApiHttpHelper()