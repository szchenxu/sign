import os
import requests

#def send_wechat(msg):
    token = '6111677c571f46edb68349777008c905'
    title = 'github'
    content = '脚本已正常执行'
    template = 'html'
    url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
    #url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
  #  print(url)
    r = requests.get(url=url)
  #  print(r.text)

if __name__ == '__main__':
    msg = '脚本已正常执行'
    send_wechat(msg)
