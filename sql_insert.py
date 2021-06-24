#导入pymysql包
import pymysql
import hashlib 
import datetime
from google_trans_new import google_translator

def insert(key,url,mesbody):
    config = {
            "host": "118.31.36.41",
            "user": "quanzu",
            "password": "quanzu_db_passowrd",
            "database": "shangtu"
        }
    # 创建数据库连接
    conn = pymysql.connect(host=config["host"],user=config["user"],password=config["password"],database=config["database"])
    #获取一个游标对象
    cursor=conn.cursor()

    # sql语句中，用%s做占位符，参数用一个元组
    # channel_id=2，channel=名人言论 ，level=2  ，is_keywords=N ,keywords_id=0,status=0，
    sql="insert into t_news_info_temp(channel_id,channel,title,url,times,mesbody,level,site,is_keywords,keywords_id,status) values(2,'名人言论',%s,%s,%s,%s,2,%s,'N',0,0)"
    
    # # title
    # hash_str = name + hashlib.sha224(mesbody.encode('utf-8')).hexdigest()

    # times
    insertTimes = (datetime.datetime.now()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    
    
    
    try:
        # 翻译成中文
        trans = google_translator()
        en2cn = trans.translate(mesbody, lang_tgt='zh-cn', lang_src='en')
    
        param=(mesbody,url,insertTimes,en2cn,'Twitter-{}'.format(key))
        #执行数据库插入操作
        cursor.execute(sql, param)

    except:
        print('Title already exists or translate connect error')
    #提交
    conn.commit()
    #关闭连接
    conn.close()
    cursor.close()


