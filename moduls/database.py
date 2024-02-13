import time

import pymongo


class DataBase:
    def __init__(self):
        self.client = pymongo.MongoClient('mongo-db', 27017)
        # self.client = pymongo.MongoClient()
        self.codes = self.client.SteamFillWeb.code

    def create_code(self, code: str, sum_: int, username: str):
        # status
        # start - Запуск
        # work - Выполняется
        # error - Ошибка
        # success - Успешно

        data = {
            'id': self.codes.count_documents({}) + 1,
            'code': code,
            'username': username,
            'sum': sum_,
            'status': 'start',
            'error': None,
            'time': int(time.time())
        }
        self.codes.insert_one(data)
        return data

    def get_code(self, code: str = None, id_: int = None):
        if id_ != None:
            return self.codes.find_one({'id': id_})
        elif code != None:
            return self.codes.find_one({'code': code})

    def edit_code(self, id_: int, js: dict):
        self.codes.update_one({"id": id_}, {"$set": js})


db = DataBase()