import httpx
import config


class SteamAPI:
    def __init__(self, token: str):
        self.client = httpx.Client(timeout=60 * 10)
        self.url = 'http://steam-cvnfdtgasoyg.nitro-store.com:8000'
        self.token = token

    def send(self, username: str, sum_: int, type_: int = 2):
        req = self.client.get(self.url + '/steam/transfer', params={
            'steam_username': username,
            'money_rub': sum_,
            'token': self.token,
            'type_': type_,
        }).json()

        return req


steam = SteamAPI(config.steam_token)

