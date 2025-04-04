import mysql.connector

from config.settings import load_config
from config.logger import setup_logging

TAG = __name__
class MysqlUtils:
    def __init__(self, config: dict):
        self.config = config
        self.logger = setup_logging()
        [self.mydb, self.mycursor] = self.open_db(config)

    def open_db(self, config):
        config = load_config()
        log_config = config["database"]
        host = log_config.get("host")
        port = log_config.get("port")
        username = log_config.get("username")
        password = log_config.get("password")
        database = log_config.get("database")

        self.logger.bind(tag=TAG).info("database://{}:{}/{}", host, port, database)

        # 建立数据库连接
        mydb = mysql.connector.connect(
            host=host,
            port=port,
            user=username,
            password=password,
            database=database
        )

        # 创建游标对象，用于执行 SQL 语句
        mycursor = mydb.cursor()
        return mydb, mycursor



    def close_db(self, ):
        # 关闭游标
        self.mycursor.close()
        # 关闭数据库连接
        self.mydb.close()


    def selectAgent(self, device_code):
        sql = """SELECT a.* FROM ai_agent a LEFT JOIN ai_device b ON a.id = b.agent_id WHERE b.id = %s """
        values = (device_code,)
        self.mycursor.execute(sql, values)
        result = self.mycursor.fetchall()
        field_names = [desc[0] for desc in self.mycursor.description]
        records = [dict(zip(field_names, row)) for row in result]
        return records