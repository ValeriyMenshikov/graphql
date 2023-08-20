import json
from modules import modules_provider as mp


class MailhogApiHttpHelper:
    def __init__(self):
        self.mailhog_api = mp.http.mailhog_api

    def get_token_from_last_email(self) -> str:
        """
        Get user activation token from last email
        :return:
        """
        # sleep(2)
        emails = self.mailhog_api.get_api_v2_messages(limit=1).json()
        data = json.loads(emails["items"][0]["Content"]["Body"])
        token_url = data.get("ConfirmationLinkUrl") or data.get("ConfirmationLinkUri")
        token = token_url.split("/")[-1]
        return token
