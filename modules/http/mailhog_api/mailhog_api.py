import requests


class MailhogApi:
    def __init__(self, host: str, disable_log=False) -> None:
        self.host = host
        self.disable_log = disable_log
        self.client = requests.session()

    def get_api_v2_messages(self, limit: int = 50) -> requests.Response:
        """
        Get messages by limit
        :param limit:
        :return:
        """
        response = self.client.get(
            url=f"{self.host}/api/v2/messages",
            params={
                'limit': limit
            }
        )
        return response
