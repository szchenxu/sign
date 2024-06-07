import os
import sys
import time
from telethon.sync import TelegramClient
# Use your own values from my.telegram.org
  
api_id = os.environ.get("TG_API_ID")
api_hash = str(os.environ.get("TG_API_HASH"))
sys.path.append('.github/workflows'）
#print(f"文件路径是：{os.getcwd()}")
client = TelegramClient('chenxu', api_id, api_hash)
client.start()
client.send_message("@chadanglaoba", '叼毛')

client.disconnect()
