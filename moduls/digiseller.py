import time
import hashlib
import traceback

import httpx
import config


class Digiseller:
    def __init__(self, key: str, seller_id: int):
        self.url = 'https://api.digiseller.ru/api'

        self.client = httpx.Client(headers={'Content-Type': 'application/json', 'Accept': 'application/json'})
        self.token: str = None

        self.key = key
        self.seller_id = seller_id

        self.login()

    def login(self):
        timestamp = int(time.time())
        req = self.client.post(self.url + '/apilogin', json={
            'seller_id': self.seller_id,
            'timestamp': timestamp,
            'sign': self.create_sign(timestamp)
        }).json()
        self.token = req['token']
        return self.token

    def create_sign(self, timestamp: int):
        return hashlib.sha256(f"{self.key}{timestamp}".encode('utf-8')).hexdigest()

    def check_unique_code(self, unique_code: str, reply: bool = True):
        try:
            req = self.client.get(self.url + f'/purchases/unique-code/{unique_code}', params={'token': self.token})
            req_js = req.json()

            if req_js['retval'] == -4 and reply:
                self.login()
                return  self.check_unique_code(unique_code, False)
		
            return req_js
        except Exception as e:
            traceback.print_exc()
            return False


digiseller = Digiseller(config.digiseller_key, config.digiseller_userid)
