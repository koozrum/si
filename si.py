import telethon
import asyncio
import time
from telethon import TelegramClient, sync
from telethon.sync import TelegramClient, events
# Настройка
# Сюда пишем api_id и api_hash | my.telegram.org
api_id =13458225
api_hash = '36a89151f15ab59b3e0f1e82c2738b6c' 

# Нужный текст для автоответчика

message = 'Сейчас вы общаетесь с ботом, администратор скоро подойдет.'

# Сам автоответчик

client = TelegramClient('bebra', api_id, api_hash)
client.start()
print(client.get_me().stringify())
print('Аккаунт валидный')
@client.on(events.NewMessage)
async def handler(event):
    time.sleep(3)
    await event.reply(message)
    time.sleep(10) # Нужно, чтоб аккаунт не улетел на банановые острова  
client.run_until_disconnected()
