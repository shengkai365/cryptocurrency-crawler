import requests 
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
