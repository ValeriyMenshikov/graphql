from functools import cached_property
from modules.http.mailhog_api.mailhog_api import MailhogApi
from vyper import v


class HTTPConnector:

    @cached_property
    def mailhog_api(self) -> MailhogApi:
        return MailhogApi(host=v.get('service.mailhog'))
