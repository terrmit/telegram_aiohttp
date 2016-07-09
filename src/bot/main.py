import os
import logging
import asyncio

from aiohttp import web
from aiotg import Bot

from bot.conf import BOT_TOKEN, WEBHOOK_URL


logging.basicConfig(level=logging.DEBUG)
bot = Bot(api_token=BOT_TOKEN)


async def first_handler(bot, update):
    await bot.send_message(
        chat_id=update['message']['chat']['id'],
        text='first',
    )


async def second_handler(bot, update):
    await bot.send_message(
        chat_id=update['message']['chat']['id'],
        text='second',
    )


async def message_router(bot, update):
    if update['message']['text'] == '1':
        await first_handler(bot, update)

    elif update['message']['text'] == '2':
        await second_handler(bot, update)

    else:
        await bot.send_message(
            chat_id=update['message']['chat']['id'],
            text='nothing',
        )


async def setwebhook(request):
    response = await bot.api_call('setWebhook', url=WEBHOOK_URL)
    if not response:
        return web.Response(text='Setting up webhook has failed')
    return web.Response(text='Webhook has been successfully set')


async def webhook(request):
    data = await request.json()
    await message_router(bot, data)
    return web.Response(text='OK')


async def init(loop):
    app = web.Application(loop=loop)

    app.router.add_route('GET', '/setwebhook', setwebhook)
    app.router.add_route('POST', '/' + BOT_TOKEN, webhook)

    return app


def main():
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init(loop))

    web.run_app(app, port=os.environ.get('PORT', '5000'))


if __name__ == '__main__':
    main()
