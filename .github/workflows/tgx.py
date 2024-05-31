import os
import sys
import time
from telethon.sync import TelegramClient
# Use your own values from my.telegram.org

#api_id = os.environ.get("TG_API_ID")
#api_hash = str(os.environ.get("TG_API_HASH"))

api_id = 23495504
api_hash = 'b8481e30c67cf38b503457ab23e804e7'

session_name = 'chenxu'
client = TelegramClient(session_name, api_id, api_hash)
client.start()
client.send_message("@aishegongkubot", '/sign')
client.send_message("@DogeSGK_bot", '/sign')
client.send_message("@yuehanbot", '/sign')
client.send_message("@sgkvipbot", '/sign')
client.send_message("@InfSGK_bot", '/sign')
client.disconnect()
