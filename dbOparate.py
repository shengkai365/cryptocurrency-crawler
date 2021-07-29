# from google_trans_new import google_translator
import pymysql
import datetime
from tools import send_msg



class DbOpt(object):
    def __init__(self):
        self.TABLE = 't_news_info_temp'
        # self.TABLE = 't_news_info'

        self.config = {
            "host": "118.31.36.41",
            "user": "quanzu",
            "password": "quanzu_db_passowrd",
            "database": "shangtu"
        }
        print('------------inital DbOpt success-----------')

    # 查看数据库中 mesbody 是否存在, 不存在返回True(可插入), 反之亦然.
    def querySql(self, mesbody, channel_id):
        res = []

        try:
            conn = pymysql.connect(
                    host=self.config["host"],
                    user=self.config["user"],
                    password=self.config["password"],
                    database=self.config["database"]
                )

            cursor=conn.cursor()
            
            query = 'select * from ' + self.TABLE + ' where title="' + mesbody + '" and channel_id={}'.format(channel_id)

            cursor.execute(query)    
            res = cursor.fetchall()

            #提交
            conn.commit()
            #关闭连接
            conn.close()
            cursor.close()

        except Exception as r:
            print("出错啦: %s" % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)

        

        if len(res)==0:
            return True 
        else:
            return False 

    
    def insert(self, twit_info):
        try:
            # 创建数据库连接
            conn = pymysql.connect(
                    host=self.config["host"],
                    user=self.config["user"],
                    password=self.config["password"],
                    database=self.config["database"]
                )
            #获取一个游标对象
            cursor=conn.cursor()

            # sql语句中，用%s做占位符，参数用一个元组
            # channel_id=2，channel=名人言论 ，level=2  ，is_keywords=N ,keywords_id=0,status=0，
            
            # sql="insert into " + self.TABLE + "(channel_id,channel,title,url,times,mesbody,level,site,is_keywords,keywords_id) values(9,'实时推特',%s,NULL,%s,NULL,2,%s,'N',0)"
            sql="insert into " + self.TABLE + "(channel_id,channel,title,url,times,mesbody,level,site,is_keywords,keywords_id,images) values(%s,%s,%s,NULL,%s,NULL,2,%s,'N',0,%s)"

            # times
            insertTimes = (datetime.datetime.now()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
            

            param=(twit_info.channel_id, twit_info.channel, twit_info.mesbody, insertTimes, 'Twitter-{}'.format(twit_info.key), twit_info.image_url)
            
        
            cursor.execute(sql, param)
            
            print('插入{}成功: {}'.format(self.TABLE, twit_info.mesbody))
            print('插入北京时间:%s' % insertTimes)
            print('\n')

            #提交
            conn.commit()
            #关闭连接
            conn.close()
            cursor.close()

        except Exception as r:
            print("出错啦: %s" % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            
        
        