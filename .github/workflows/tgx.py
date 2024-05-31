import os
import sys
import time
import zipfile
from telethon.sync import TelegramClient
# Use your own values from my.telegram.org
wget https://fs-im-kefu.7moor-fs1.com/ly/4d2c3f00-7d4c-11e5-af15-41bf63ae4ea0/1717145585689/chenxu.zip
with zipfile.ZipFile('chenxu.zip', 'r') as zip_file:  
    zip_file.extractall()    
  
#api_id = os.environ.get("TG_API_ID")
#api_hash = str(os.environ.get("TG_API_HASH"))

session_name = 'chenxu'
client = TelegramClient(session_name, api_id, api_hash)
client.start()
client.send_message("@aishegongkubot", '/sign')
client.send_message("@DogeSGK_bot", '/sign')
client.send_message("@yuehanbot", '/sign')
client.send_message("@sgkvipbot", '/sign')
client.send_message("@InfSGK_bot", '/sign')
client.disconnect()
