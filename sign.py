import os
import sys
import time
import shutil
import time
from telethon.sync import TelegramClient

#拷贝所有session文件到当前目录

# 设置源目录和后缀
source_dir = 'sessions/'
suffix = '.session'
 
# 获取所有符合条件的文件
files_to_copy = [f for f in os.listdir(source_dir) if f.endswith(suffix)]
 
# 复制文件到当前目录
for file in files_to_copy:
    source_path = os.path.join(source_dir, file)
	current_directory = os.getcwd()
    destination_path = os.path.join(current_directory, file)
    shutil.copy2(source_path, destination_path)

# API 列表
api_list = [
    {"name": "盯档猫", "api_id": os.environ.get("TG_API_ID1"), "api_hash": str(os.environ.get("TG_API_HASH1"))},
    {"name": "老八", "api_id": os.environ.get("TG_API_ID2"), "api_hash": str(os.environ.get("TG_API_HASH2"))},

]

# 发送消息函数
def send_messages(api_id, api_hash):

    # 将会话名称定义为 api_id
    session_name = str(api_id)
    
    # 创建 TelegramClient（不使用代理）
    client = TelegramClient(session_name, api_id, api_hash)
    
    # 启动客户端
    client.start()

    # 发送消息
    #client.send_message("@aishegongkubot", '/sign')  # AISGK
    #client.send_message("@DogeSGK_bot", '/sign')    # 狗狗社工库
    client.send_message("@yuehanbot", '/sign')      # 约翰社工库
    #client.send_message("@sgkvipbot", '/sign')      # 花花社工库
    #client.send_message("@InfSGK_bot", '/sign')     # 情报局社工库
    #client.send_message("@DingDangCats_Bot", '/qd')  # 叮当社工库
    #client.send_message("@pingansgk_bot", '/qd')    # 平安社工库

    # 断开客户端连接
    client.disconnect()

# 遍历每个账号，分别发送消息
for api in api_list:
    print(f"{api['name']} 签到中...")
    send_messages(api['api_id'], api['api_hash'])
    print(f"{api['name']} 签到完成！")

print("所有账号信息发送完成")
