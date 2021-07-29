# from google_trans_new import google_translator
import pymysql
import datetime
from dbOparate import DbOpt
from crawlerTwitter import CrawlerTwit
from time import sleep
from mainTwitterServer import run 
from pytwitterscraper import TwitterScraper
from tools import send_msg 

def test_with_temp_db(TIME):
    TABLE = 't_news_info_temp'
    run(TABLE,TIME)


if __name__=="__main__":
    # ----------------------- |
    # 用副表测试整个系统
    # 4h 以内的推特
    test_with_temp_db(4*60*60)
    # ----------------------——  |