# from google_trans_new import google_translator
import pymysql
import datetime
from post import send_msg



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

    # 查看数据库中 mesbody 是否存在, 不存在返回True(可插入), 反之亦然.
    def querySql(self, mesbody):

        conn = pymysql.connect(
                host=self.config["host"],
                user=self.config["user"],
                password=self.config["password"],
                database=self.config["database"]
            )

        cursor=conn.cursor()
        
        query = 'select * from ' + self.TABLE + ' where title="' + mesbody + '" and channel_id=9' +  ' order by  id  desc limit 1'

        res = []
        try:
            cursor.execute(query)    
            res = cursor.fetchall()
        except Exception as r:
            print("出错啦: %s" % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)

        #提交
        conn.commit()
        #关闭连接
        conn.close()
        cursor.close()

        if len(res)==0:
            return True 
        else:
            return False 

    
    def insert(self, key, msg):
        
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
        
        sql="insert into " + self.TABLE + "(channel_id,channel,title,url,times,mesbody,level,site,is_keywords,keywords_id) values(9,'实时推特',%s,NULL,%s,NULL,2,%s,'N',0)"

        # times
        insertTimes = (datetime.datetime.now()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

        mesbody = key + '：'+ msg
        param=(mesbody, insertTimes, 'Twitter-{}'.format(key))
        
        can_insert = self.querySql(mesbody)

        try:
            if can_insert:

                #！！！！！！！！！！|
                cursor.execute(sql, param)
                #！！！！！！！！！！|

                #！！！！！！！！！！|
                # send_msg(mesbody)
                #！！！！！！！！！！|
                
            else:
                print('data exist')

        except Exception as r:
            print("出错啦: %s" % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            
        
        #提交
        conn.commit()
        #关闭连接
        conn.close()
        cursor.close()