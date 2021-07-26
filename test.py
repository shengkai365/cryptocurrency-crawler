# from google_trans_new import google_translator
import pymysql
import datetime
from dbOparate import DbOpt
from crawlerTwitter import CrawlerTwit
from time import sleep
from mainTwitterServer import run 
from pytwitterscraper import TwitterScraper
from post import send_msg 

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
        print(craw_data)
        
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

def test_post(mesbody, channel):
    send_msg(mesbody, channel)

if __name__=="__main__":

    # ----------------------- |
    # 测试数据插入是否正常
    # 注释 send_msg!!!!!!!!!!
    # key = '马斯克'
    # msg = 'Congrats Tesla Team on over 200,000 car built &amp; delivered in Q2'
    # test_db(key, msg)
    # ----------------------——  |

    # ----------------------- |
    # 测试数据爬取是否正常
    # test_crawler()
    # ----------------------——  |


    # ----------------------- |
    # 用副表测试整个系统
    # 4h 以内的推特
    test_with_temp_db(4*60*60)
    # ----------------------——  |


    # ----------------------- |
    # 测试mesbody的完整性
    # test_full_mesbody_1()
    # print('--------------分割线----------------')
    # test_full_mesbody_2()
    # ----------------------——  |

    # ----------------------- |
    # 测试post是否出错
    # mesbody = '推特 | BabyDoge：If this gets retweeted by @ElonMusk or @cz_binance We will donate $100,000.00 to a dog rescue of their choice! #BabyDoge 🐶🍼#SaveDogs'
    # channel =  '实时推特'
    # test_post(mesbody, channel)
    # ----------------------——  |