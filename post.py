import requests 
import urllib3
from urllib.parse import urlencode


def send_msg(mesbody,channel):
    try:
        url = "https://bpj-s.junshangxun.com/sendmessage"
        values = {
            "title": mesbody,
            "channel" :channel
        }
        a = requests.post(url, json=values)
        print(a)
        
    except Exception as r:
        print("出错啦: %s" % r)
        print(r.__traceback__.tb_frame.f_globals["__file__"])
        print(r.__traceback__.tb_lineno)

# def send_msg_urllib3(mesbody, channel):
#     try:
#         url = "https://bpj-s.junshangxun.com/sendmessage"
#         values = {
#             "title": mesbody,
#             "channel" :channel
#         }
#         http = urllib3.PoolManager()
#         encoded_data = urlencode(values)
#         r = http.request('POST',
#             'http://localhost:8080/assets?'+encoded_data,
#             headers={'Content-Type':'application/json'})  
#         print(r)

#     except Exception as r:
#         print("出错啦: %s" % r)
#         print(r.__traceback__.tb_frame.f_globals["__file__"])
#         print(r.__traceback__.tb_lineno)

