import os
import requests
import json
token = str(os.environ.get("TG_API_HASH1")) #在pushpush网站中可以找到
title= 'github' #改成你要的标题内容
content ='脚本已正常执行' #改成你要的正文内容
url = 'http://www.pushplus.plus/send'
data = {
    "token":token,
    "title":title,
    "content":content
}
body=json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type':'application/json'}
requests.post(url,data=body,headers=headers)
