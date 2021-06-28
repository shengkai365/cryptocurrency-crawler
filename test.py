# from google_trans_new import google_translator
import pymysql
import datetime
from post import send_msg

def search(title):
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

    querySql = 'select * from t_news_info_temp where title="' + title +  '" order by  id  desc limit 1'
    
    cursor.execute(querySql)
    lines = cursor.fetchall()
    
    #提交
    conn.commit()
    #关闭连接
    conn.close()
    cursor.close()
    return lines 

