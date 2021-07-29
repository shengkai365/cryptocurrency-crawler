import datetime
import time
def generateHTML(twit_info, save_path):
    GEN_HTML_PATH = save_path + twit_info.name + str(time.time())[-7:] + '.html' # 命名生成的html

    title= '推特 | ' + twit_info.key 
    mesbody = twit_info.msg 

    dt = datetime.datetime.now()+datetime.timedelta(hours=8)
    nowtime = dt.strftime("%Y-%m-%d %H:%M:%S")
    

    html = """
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="utf-8" />
        <meta
        name="viewport"
        content="width=device-width, initial-scale=1.0, user-scalable=0"
        />
        <meta content="yes" name="apple-mobile-web-app-capable" />
        <meta content="black" name="apple-mobile-web-app-status-bar-style" />
        <meta content="telephone=no" name="format-detection" />
        <title>html模板</title>
    </head>
    <body>
        <div class="box-warp">
        <div class="top-box">
            <div class="title">
            <!-- eg: 推特｜MidiDoge:MiniDOGE fadsfasdfasadfasdfasdfad -->
            <p>%s</p>
            </div>
            <!-- eg: 2020-01-01 12:11:22 -->
            <div class="time">%s</div>
        </div>
        <div class="content">
            <!-- To celebrate the #Tokyo2020 starting today, this #OKExWeekendQuiz we are bringing the #Olympics quiz!What are the 5 sports on the logo?1⃣️ Follow+ Like+ Retweet2⃣️ Comment with the right hashtags (e.g. #football )3⃣️ Fill  -->
            %s
        </div>
        <div class="image-box">"""%(title,nowtime,mesbody)

    for i in range(len(twit_info.image_urls_list)):
        html += """
            <div class="image-item">
            <img src="%s" alt="" srcset="">
            </div>"""%twit_info.image_urls_list[i]
        
    html += """
        </div>
        </div>
        <script>
        $(function () {});
        </script>
    </body>
    <style>
        *{padding:0;margin:0}body{background-color:#e2e2e2}.box-warp{background-color:white;margin:10px 8px 0 8px;border-radius:5px}.box-warp .top-box{border-bottom:1px solid #d8d5d5;padding:10px}.box-warp .top-box .title{font-weight:bold;font-size:1.2rem;width:100%}.box-warp .top-box .title p{word-break:normal;word-break:break-all}.box-warp .top-box .time{font-size:.89rem;color:#9e9e9e;margin-top:5px}.box-warp .content{padding:20px 10px 0 10px;font-size:1rem}.box-warp .content p{word-break:normal;word-break:break-all}.image-box{margin-top:20px}.image-box .image-item{margin-top:5px;padding:0 10px}.image-box .image-item img{width:100%;border-radius:5px}
    </style>
    </html>"""

    with open(GEN_HTML_PATH,'w',encoding='utf-8') as f:
        f.write(html)
    return GEN_HTML_PATH 


import requests 
def send_msg(mesbody, channel, image_url, html_url):
    try:
        url = "https://bpj-s.junshangxun.com/sendmessage"
        values = {
            "title": mesbody,
            "channel": channel,
            "mesbody": image_url,
            "urls": html_url
        }
        a = requests.post(url, json=values)
        print(a, '发送成功')

        
    except Exception as r:
        print("----发送企业微信失败----")
        print("出错啦: %s" % r)
        print(r.__traceback__.tb_frame.f_globals["__file__"])
        print(r.__traceback__.tb_lineno)


# 安装
# pip install python-Levenshtein
# pip install fuzzywuzzy
from fuzzywuzzy import fuzz
from difflib import SequenceMatcher
def is_similar(title1, title2, threshold=0.5):

    # difflib
    sequenceMatcher = SequenceMatcher()
    sequenceMatcher.set_seqs(title1, title2)
    sml1 = sequenceMatcher.ratio()

    sml2 = fuzz.ratio(title1, title2)
    print(sml1,sml2)
    if sml1 > threshold and sml2>threshold:
        return True 
    return False 