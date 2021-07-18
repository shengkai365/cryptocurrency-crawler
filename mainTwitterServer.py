from time import sleep 
import datetime 
from crawlerTwitter import CrawlerTwit
from dbOparate import DbOpt 
from ImageAddressTransfer import Oss
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

def run(TABLE='',TIME=305):
    db_opt = DbOpt()
    db_opt.TABLE = TABLE
    
    while True:
        for key in users.keys():
            craw = CrawlerTwit(users[key])
            craw_data = craw.get_datas()

            now = datetime.datetime.now()
            for msg, time, urls in craw_data:

                # delta_time = (now-time).seconds
                delta_time = now.timestamp()-time.timestamp()
                # 超过5分钟不入库
                if delta_time > TIME:
                    continue 
                
                image_urls = []
                try:
                    oss = Oss()
                    image_urls = oss.transfer(urls)
                except Exception as r:
                    print("出错啦: %s" % r)
                    print(r.__traceback__.tb_frame.f_globals["__file__"])
                    print(r.__traceback__.tb_lineno)

                db_opt.insert(key, msg, image_urls)


        print("Waite 5 minutes")
        sleep(300)


if __name__=="__main__":
    
    # 设置正表还是副表
    TABLE='t_news_info'
    run(TABLE)