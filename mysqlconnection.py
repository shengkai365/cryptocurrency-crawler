# encoding=utf-8
import pymysql
# 导入所有Mysql配置常量,请自行指定文件


'''
DB 链接基础工具类
'''
class MysqlConnection(object):
    """
    mysql操作类，对mysql数据库进行增删改查
    """
    def __init__(self, config):
        # Connect to the database
        self.connection = pymysql.connect(**config)
        self.connection.autocommit(True)
        self.cursor = self.connection.cursor()

    def QueryAll(self, sql):
        """
        查询所有数据
        :param sql:
        :return:
        """
        # 数据库若断开即重连
        self.reConnect()

        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def QueryMany(self, sql, n):
        """
        查询某几条数据数据
        :param sql:
        :return:
        """
        # 数据库若断开即重连
        self.reConnect()

        self.cursor.execute(sql)
        return self.cursor.fetchmany(n)

    def QueryOne(self, sql) -> object:
        """
        查询某几条数据数据
        :param sql:
        :return:
        """
        # 数据库若断开即重连
        self.reConnect()

        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # return self.cursor.fetchone()

    def reConnect(self):
        """
        重连机制
        :return:
        """
        try:
            self.connection.ping()
        except:
            self.connection()

    def Operate(self, sql, params=None, DML=True):
        """
        数据库操作:增删改查
        DML: insert / update / delete
        DDL: CREATE TABLE/VIEW/INDEX/SYN/CLUSTER
        """
        try:
            # 数据库若断开即重连
            self.reConnect()

            with self.connection.cursor() as cursor:
                cursor.execute(sql, params)

                self.connection.commit()

        except Exception as e:
            if DML:
                # 涉及DML操作时,若抛异常需要回滚
                self.connection.rollback()
            print(e)

    def __del__(self):
        """
        MysqlConnection实例对象被释放时调用此方法,用于关闭cursor和connection连接
        """
        self.cursor.close()
        self.connection.close()