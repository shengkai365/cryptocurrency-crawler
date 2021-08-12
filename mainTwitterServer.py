from time import sleep 
import datetime 
from crawlerTwitter import CrawlerTwit
from dbOparate import DbOpt 
from ImageAddressTransfer import Oss
from tools import generateHTML
from crawlerTwitter import TwitterInfo
from tools import send_msg

# users = {   
#         '马斯克':'elonmusk',
#         'Coinbase':'CoinbasePro', 
#         '孙宇晨':'justinsuntron',
#         '赵长鹏':'cz_binance',
#         '灰度创始人':'BarrySilbert',
#         '火币': 'HuobiGlobal',
#         '灰度资本': 'Grayscale',
#         '欧易': 'OKEx',
#         'Butter':'butterswap',
#         'MiniDoge':'MiniDOGEToken',
#         'BabyDoge':'BabyDogeCoin'
#     }
users = {   
        'Coinbase':'CoinbasePro'
    }
account = {
            'AccessKeyID': '******',
            'AccessKeySecret': '*******',
            'BucketName': 'bpj-webfiles',
            'ImagePath' : 'images/twitter/'
        }

HTML_SAVE_PATH = '/root/twitter-html/'

def run(TABLE, TIME=120):
    db_opt = DbOpt()
    db_opt.TABLE = TABLE
    count = 0

    while True:
        for key in users.keys():
            craw = CrawlerTwit(users[key])
            craw_data = craw.get_datas()

            now = datetime.datetime.now()
            for msg, time, urls in craw_data:

                # delta_time = (now-time).seconds
                delta_time = now.timestamp()-time.timestamp()
                # 超过2分钟不入库
                if delta_time > TIME:
                    continue 
                
                twit_info = TwitterInfo(key, msg, users[key])
                can_insert = db_opt.querySql(twit_info.mesbody, twit_info.channel_id)
                # 数据存在不入库
                if not can_insert:
                    print('data exist: {}'.format(twit_info.mesbody))
                    continue 

               
                oss = Oss(account)
                
                image_urls = oss.transfer(urls)
                twit_info.inital_oss_image_url(image_urls)
                print('上传图片地址：',twit_info.image_urls_list)

                GEN_HTML_LOCAL_PATH = generateHTML(twit_info, HTML_SAVE_PATH)
                html_url = oss.put_HTML_to_oss(GEN_HTML_LOCAL_PATH)
                print('上传html地址：', html_url)

                twit_info.inital_oss_html_url(html_url)

                #！！！！！！！！！！|
                # 如果是正表, 发送企业微信
                if db_opt.TABLE=='t_news_info':
                    send_msg(twit_info)
                    send_msg(twit_info)
                    send_msg(twit_info)
                #！！！！！！！！！！|
                db_opt.insert(twit_info)

                
        count += 1
        print("--------------step%s%s%s%s%s---------------"%(count,count,count,count,count))
        print("\n\n")


if __name__=="__main__":
    
    # 设置正表还是副表
    TABLE='t_news_info'
    run(TABLE)