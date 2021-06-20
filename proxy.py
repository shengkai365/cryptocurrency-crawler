import requests
import json
import random 
from time import sleep 
#请求地址

# ip_url : ip池链接地址，json格式
# ip_pool: 获取的ip池，字典格式
def get_ip_pool(ip_url):
    text = requests.get(ip_url).text
    print(text)
    ip_pool = json.loads(text)["data"]
    
    return ip_pool 

# ip_item: 形如{"ip":"117.69.179.6","port":4284"} 的字典
def random_ip(ip_pool):
    length = len(ip_pool)
    rand_index = random.randint(0,length-1)
    ip_item = ip_pool[rand_index]
    return ip_item 


def http_proxy(ip_item):
    proxyHost = ip_item["ip"]
    proxyPort = ip_item["port"]
    proxyMeta = "http://%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
    }
    proxies = {
        "http"  : proxyMeta,
        "https"  : proxyMeta
    }
    return proxies 

def socks5_proxy(ip_item):
    proxyHost = ip_item["ip"]
    print("提取",proxyHost)
    proxyPort = ip_item["port"]
    #pip install -U requests[socks]  socks5 
    proxyMeta = "socks5://%(host)s:%(port)s" % {
        "host" : proxyHost,
        "port" : proxyPort,
    }
    proxies = {
        "http"  : proxyMeta,
        "https"  : proxyMeta
    }
    return proxies 



ip_url = 'http://webapi.http.zhimacangku.com/getip?num=20&type=2&pro=&city=0&yys=0&port=2&time=1&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
ip_pool = get_ip_pool(ip_url)
while True:
    ip_item = random_ip(ip_pool)
    proxies = socks5_proxy(ip_item)

    targetUrl = "http://httpbin.org/ip"

    resp = requests.get(targetUrl,proxies=proxies)
    # print(resp.status_code)
    print("使用",resp.text)




