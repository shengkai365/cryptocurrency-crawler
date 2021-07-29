from time import sleep 
import datetime 
from crawlerTwitter import CrawlerTwit
from dbOparate import DbOpt 
from ImageAddressTransfer import Oss
from tools import generateHTML
from crawlerTwitter import TwitterInfo

users = {   
        '马斯克':'elonmusk',
        'Coinbase':'CoinbasePro', 
        '孙宇晨':'justinsuntron',
        '赵长鹏':'cz_binance',
        '灰度创始人':'BarrySilbert',
        '火币': 'HuobiGlobal',
        '灰度资本': 'Grayscale',
        '欧易': 'OKEx',
        'Butter':'butterswap',
        'MiniDoge':'MiniDOGEToken',
        'BabyDoge':'BabyDogeCoin'
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
                
                twit_info = TwitterInfo(key, msg, users[key])
                can_insert = db_opt.querySql(twit_info.mesbody, twit_info.channel_id)

                # 超过2分钟不入库
                if delta_time > TIME or not can_insert:
                    continue 
                
               
                oss = Oss(account)
                image_urls = oss.transfer(urls)
                twit_info.inital_oss_image_url(image_urls)

                GEN_HTML_LOCAL_PATH = generateHTML(twit_info, HTML_SAVE_PATH)
                HTML_url = oss.put_HTML_to_oss(GEN_HTML_LOCAL_PATH)
                    

                twit_info.inital_oss_html_url(HTML_url)
                
                db_opt.insert(twit_info)
                
        count += 1
        print("--------------step%s---------------"%count)


if __name__=="__main__":
    
    # 设置正表还是副表
    TABLE='t_news_info'
    run(TABLE)