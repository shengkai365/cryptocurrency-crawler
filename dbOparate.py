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

    
    def insert(self, key, msg, image_urls):
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


            channel_id = -1
            channel = ' '

            if key in {'Butter','MiniDoge','BabyDoge'}:
                channel_id = 16
                channel = '项目推特'
            
            if key in {'孙宇晨','赵长鹏','马斯克','灰度创始人'}:
                channel_id = 2
                channel = '名人推特'
            
            if key in {'火币','灰度资本','欧易','Coinbase'}:
                channel_id = 9
                channel = '平台推特'
        


            # times
            insertTimes = (datetime.datetime.now()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
            
            mesbody = '推特 | ' + key + '：'+ msg
            
            # 暂时取前一个地址
            image_url = '' if image_urls==[] else ','.join(image_urls)

            param=(channel_id, channel, mesbody, insertTimes, 'Twitter-{}'.format(key),image_url)
            
            can_insert = self.querySql(mesbody, channel_id)

        
            if can_insert:
                print("准备插入: %s" % mesbody[:20])
                #！！！！！！！！！！|
                cursor.execute(sql, param)
                #！！！！！！！！！！|

                #！！！！！！！！！！|
                # 如果是正表, 发送企业微信
                if self.TABLE=='t_news_info':
                    send_msg(mesbody,channel,image_url)
                #！！！！！！！！！！|
                
                print('插入{}成功: {}'.format(self.TABLE, mesbody))
                print('插入北京时间:%s' % insertTimes)

            else:
                print('data exist: {}'.format(mesbody))

            print('\n\n')
            #提交
            conn.commit()
            #关闭连接
            conn.close()
            cursor.close()

        except Exception as r:
            print("出错啦: %s" % r)
            print(r.__traceback__.tb_frame.f_globals["__file__"])
            print(r.__traceback__.tb_lineno)
            
        
        