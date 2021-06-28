# from google_trans_new import google_translator
import pymysql
import datetime
from post import send_msg

def insert(key,mesbody):
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
    
    sql="insert into t_news_info(channel_id,channel,title,url,times,mesbody,level,site,is_keywords,keywords_id) values(9,'实时推特',%s,NULL,%s,NULL,2,%s,'N',0)"

    # times
    insertTimes = (datetime.datetime.now()+datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")

    mesbody = key + '：'+ mesbody 
    param=(mesbody, insertTimes, 'Twitter-{}'.format(key))
    
    querySql = 'select * from t_news_info_temp where title="' + mesbody + '" and channel_id=9' +  ' order by  id  desc limit 1'
    try:
        # # 翻译成中文
        # trans = google_translator()
        # en2cn = trans.translate(mesbody, lang_tgt='zh-cn', lang_src='en')
        
        cursor.execute(querySql)    
        lines = cursor.fetchall()

        #执行数据库插入操作
        if len(lines)==0:
            cursor.execute(sql, param)
            send_msg(mesbody)
        else:
            print('data exist')
            print(mesbody)
    except:
        print('Title already exists')
    #提交
    conn.commit()
    #关闭连接
    conn.close()
    cursor.close()

