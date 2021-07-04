# from google_trans_new import google_translator
import pymysql
import datetime
from dbOparate import DbOpt
from crawlerTwitter import CrawlerTwit
from time import sleep
from mainTwitterServer import run 
from pytwitterscraper import TwitterScraper

users = {   
    '马斯克':'elonmusk',
    'Coinbase':'CoinbasePro', 
    '孙宇晨':'justinsuntron',
    '赵长鹏':'cz_binance',
    '灰度创始人':'BarrySilbert',
}

def test_db(key, msg):
    db_opt = DbOpt()
    db_opt.TABLE = 't_news_info_temp'
    db_opt.insert(key, msg)


def test_crawler(TIME=300):
    for key in users.keys():
            print('---------start---------')
            craw = CrawlerTwit(users[key])
            craw_data = craw.get_datas()

            now = datetime.datetime.now()
            for msg,time in craw_data:
                
                print('now:',now)
                print('time:',time)
                delta_time = (now.timestamp()-time.timestamp())
                print('delta_time', delta_time)
                print('msg', msg)
                
                # 超过5分钟不入库
                if delta_time > TIME:
                    continue 
            
                print("尝试插入: %s"% msg)
            print('---------end------------\n\n\n')

def test_with_temp_db(TIME):
    TABLE = 't_news_info_temp'
    run(TABLE,TIME)


def test_full_mesbody_1():
    # 方法一：
    tw = TwitterScraper()
    profile = tw.get_profile(name='justinsuntron')
    id = profile.__dict__['id']

    #tw.get_tweets(int(id), count=3)
    tweets = tw.get_tweets(id, count=3)
    for line in tweets.contents:
        print(line['text'])


def test_full_mesbody_2():
    # 方法二：
    tw = TwitterScraper()
    profile = tw.get_profile(name='justinsuntron')
    id = profile.__dict__['id']

    tweets = tw.get_tweets(id, count=3)
    for line in tweets.contents:
        
        twinfo = tw.get_tweetinfo(line['id'])
        print(twinfo.contents['text'])



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
    # test_crawler()
    # ----------------------——  |


    # ----------------------- |
    # 用副表测试整个系统
    # 10h 以内的推特
    test_with_temp_db(36000)
    # ----------------------——  |


    # ----------------------- |
    # 测试mesbody的完整性
    # test_full_mesbody_1()
    # print('--------------分割线----------------')
    # test_full_mesbody_2()
    # ----------------------——  |