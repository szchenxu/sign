import os
import requests

def send_wechat(msg):
    token = os.environ.get("WECHATPUSH_TOKEN")
    title = 'github'
    content = msg
    template = 'html'
    url = f"https://www.pushplus.plus/send?token={token}&title={title}&content={content}&template={template}"
  #  print(url)
    r = requests.get(url=url)
  #  print(r.text)

if __name__ == '__main__':
    msg = '脚本已正常执行'
    send_wechat(msg)
