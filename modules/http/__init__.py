from functools import cached_property
from modules.http.mailhog_api.mailhog_api import MailhogApi
from config.config import settings


class HTTPConnector:

    @cached_property
    def mailhog_api(self) -> MailhogApi:
        return MailhogApi(host=settings.service.mailhog)
