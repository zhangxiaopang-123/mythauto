import pymysql


class SQL:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    def sql_select(self, sql):
        db = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            port=self.port,
            db=self.database
        )
        cursor = db.cursor()
        cursor.execute(sql)
        demo = cursor.fetchall()
        db.commit()
        db.close()
        # print(demo[0])
        return demo

    def sql_insert(self, sql):
        db = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            port=self.port,
            db=self.database
        )
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()

    def sql_delete(self, sql):
        db = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            port=self.port,
            db=self.database
        )
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()

    def sql_select_result(self, sql):
        db = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            port=self.port,
            db=self.database
        )
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        result = cursor.fetchall()
        db.close()
        return result[-1]

    def sql_update(self, sql):
        db = pymysql.connect(
            host=self.host,
            user=self.user,
            passwd=self.password,
            port=self.port,
            db=self.database
        )
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()

