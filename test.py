# from google_trans_new import google_translator
import pymysql
import datetime
from dbOparate import DbOpt
from crawlerTwitter import CrawlerTwit
users = {   
    '马斯克':'elonmusk',
    'Coinbase':'CoinbasePro', 
    '孙宇晨':'justinsuntron',
    '赵长鹏':'cz_binance',
    '灰度创始人':'BarrySilbert'
}
def test_db(key, msg):
    db_opt = DbOpt()
    db_opt.TABLE = 't_news_info_temp'
    db_opt.insert(key, msg)


def test_crawler():
    for key in users.keys():
            craw = CrawlerTwit(users[key])
            craw_data = craw.get_datas()

            now = datetime.datetime.now()
            for msg,time in craw_data:
                print('now:',now)
                print('time:',time)
                delta_time = (now.timestamp()-time.timestamp())
                print('delta_time', delta_time)
                # 超过5分钟不入库
                if delta_time > 300:
                    continue 
                else:
                    print("尝试插入: %s"% msg)

if __name__=="__main__":

    # ----------------------- |
    # 测试数据插入是否正常
    # 注释 send_msg!!!!!!!!!!
    # key = ''
    # msg = ''
    # test_db(key, msg)
    # ----------------------——  |

    # ----------------------- |
    # 测试数据爬取是否正常
    test_crawler()
    # ----------------------——  |

