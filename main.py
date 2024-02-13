import traceback

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from multiprocessing import Process
import config
from moduls.digiseller import digiseller
from moduls.database import db
from moduls.other import telegram_logging, steam_send_money
from fastapi.responses import RedirectResponse


templates = Jinja2Templates(directory="templates")


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post("/steam")
async def steam_post_req(request: Request, uniquecode: str = None):
    return RedirectResponse(url=f"/steam?uniquecode={uniquecode}", status_code=303)


@app.get("/steam")
async def steam_req(request: Request, uniquecode: str = None):
    if not uniquecode:
        return {'error': 'uniquecode is None'}

    result = digiseller.check_unique_code(uniquecode)

    if not result:
        return templates.TemplateResponse("error.html", {"request": request})
    if result['retval'] == -2 or result['retval'] == 1:
        return {'error': 'unique_code invalid'}
    if result['retval'] != 0:
        return {'error': f'reval is {result["retval"]}'}

    db_reuslt = db.get_code(code=uniquecode)

    if not db_reuslt:
        try:
            username = list(filter(lambda x: x['id'] in config.digiseller_optionsid, result['options']))[0]['value']
        except:
            traceback.print_exc()
            return {'error': 'Get params'}
        sum_ = result['cnt_goods']

        db_reuslt = db.create_code(uniquecode, sum_, username)

        Process(target=steam_send_money, args=(db_reuslt['id'], )).start()
        telegram_logging(f'Уникальный код #{uniquecode}_{db_reuslt["id"]} активирован!\n\nСумма: {sum_}\nЮзернейм: {username}')

    error_massage = None
    if db_reuslt['error'] == 'User not found':
        error_massage = 'юзернейм неверный'

    return templates.TemplateResponse("steam.html",
                                      {"request": request, 'status': db_reuslt['status'], 'sum': db_reuslt['sum'],
                                       'username': db_reuslt['username'], 'error_massage': error_massage,
                                       'buy_url': f'https://oplata.info/info/buy.asp?id_i={result.get("inv")}&lang=ru-RU'})
