import os
import sys
import time
import shutil
from telethon.sync import TelegramClient
# Use your own values from my.telegram.org
#sys.path.append('..')

source_file_path = '.github/workflows/chenxu.session'
# 获取当前目录
current_directory = os.getcwd()
# 目标文件路径
destination_file_path = os.path.join(current_directory, 'chenxu.session')
# 复制文件
shutil.copy2(source_file_path, destination_file_path)

api_id = os.environ.get("TG_API_ID")
api_hash = str(os.environ.get("TG_API_HASH"))
#print(f"文件路径是：{os.getcwd()}")
client = TelegramClient('chenxu', api_id, api_hash)
client.start()
client.send_message("@chadanglaoba", '叼毛')

client.disconnect()
