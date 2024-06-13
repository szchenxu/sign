import os
import sys
import time
import shutil
from telethon.sync import TelegramClient

#session文件目录
source_file_path = 'sessions/session1.session'
# 获取当前目录
current_directory = os.getcwd()
# 目标文件路径
destination_file_path = os.path.join(current_directory, 'session1.session')
# 复制文件
shutil.copy2(source_file_path, destination_file_path)

api_id = os.environ.get("TG_API_ID1")
api_hash = str(os.environ.get("TG_API_HASH1"))
#通过环境变量获取api

client = TelegramClient('session1', api_id, api_hash)
client.start()
#客户端登录

client.send_message("@aishegongkubot", '/sign')
client.send_message("@DogeSGK_bot", '/sign')
client.send_message("@yuehanbot", '/sign')
client.send_message("@sgkvipbot", '/sign')
client.send_message("@InfSGK_bot", '/sign')
client.send_message("@DingDangCats_Bot", '/qd')
client.send_message("@pingansgk_bot", '/qd')
#发送其他签到消息此处自行添加...

client.disconnect()
