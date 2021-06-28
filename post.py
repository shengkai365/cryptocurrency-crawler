import requests 
def send_msg(mesbody):
    try:
        url = "https://bpj-s.junshangxun.com/sendmessage"
        values = {
            "title": mesbody 
        }
        a = requests.post(url, json=values)
        print(a)
        
    except Exception as r:
        print("未知错误 %s"%r)