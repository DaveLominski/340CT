import pymysql
import logInWindow

class userDB:
    def __init__(self):

        self.conn = pymysql.connect(host='localhost',
                                    port=3306, user='root',
                                    passwd='', db='smart_mart')

        self.cur = self.conn.cursor()


    def query(self,sql):
        self.cur.execute(sql)
        self.conn.commit()
        self.closeDB()

    def getData(self,sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchone()[0]
        except:
            pass

    def closeDB(self):
        self.conn.close()


class itemDB:

    def __init__(self):

        self.conn = pymysql.connect(host='localhost',
                                    port=3306, user='root',
                                    passwd='', db='smart_mart')

        self.cur = self.conn.cursor()


    def query(self,sql):
        self.cur.execute(sql)
        self.conn.commit()
        self.closeDB()

    def getData(self,sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except:
            pass

    def getOneData(self,sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchone()[0]
        except:
            pass



    def closeDB(self):
        self.conn.close()
