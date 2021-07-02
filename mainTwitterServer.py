from time import sleep 
import datetime 
from crawlerTwitter import CrawlerTwit
from dbOparate import DbOpt 

users = {   
        '马斯克':'elonmusk',
        'Coinbase':'CoinbasePro', 
        '孙宇晨':'justinsuntron',
        '赵长鹏':'cz_binance',
        '灰度创始人':'BarrySilbert',
    }

def run(TABLE='',TIME=300):
    db_opt = DbOpt()
    db_opt.TABLE = TABLE
    
    while True:
        for key in users.keys():
            craw = CrawlerTwit(users[key])
            craw_data = craw.get_datas()

            now = datetime.datetime.now()
            for msg, time in craw_data:

                # delta_time = (now-time).seconds
                delta_time = now.timestamp()-time.timestamp()
                # 超过5分钟不入库
                if delta_time > TIME:
                    continue 
                db_opt.insert(key, msg)


        print("Waite 5 minutes")
        sleep(300)


if __name__=="__main__":
    
    # 设置正表还是副表
    TABLE='t_news_info'
    run(TABLE)