from moduls.database import db
from moduls.steam import steam
import httpx
import config


def telegram_logging(text):
    for chat_id in config.telegram_id:
        r = httpx.get(f"https://api.telegram.org/bot{config.telegram_token}/sendMessage", params={'chat_id': chat_id, 'text': text})


def steam_send_money(db_id: int):
    db_reuslt = db.get_code(id_=db_id)

    db.edit_code(db_id, {'status': 'work'})
    result = steam.send(db_reuslt['username'], db_reuslt['sum'])
    if result.get('error'):
        db.edit_code(db_id, {'status': 'error', 'error': result.get('message')})
        telegram_logging(f'Уникальный код #{db_reuslt["code"]}_{db_reuslt["id"]} ошибка!\n\nОтвет сервера: {result}')
    else:
        db.edit_code(db_id, {'status': 'success'})
        telegram_logging(f'Уникальный код #{db_reuslt["code"]}_{db_reuslt["id"]} выдан!')
