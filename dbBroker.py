'''The whole file is a dbBroker, meaning that if another file needs to use the database, it can reuse the classes and
    functions from this file. This increases the re-usability and simplifies the whole program by breaking down each
    component. The functions are easy to use, as most of them just need a SQL statement inputted as an attribute '''
import pymysql


'''A class that takes care of connecting to the database but also doing simple functions'''
class userDB:
    '''Initialises the connection to the database'''
    def __init__(self):

        self.conn = pymysql.connect(host='localhost',
                                    port=3306, user='root',
                                    passwd='', db='smart_mart')

        self.cur = self.conn.cursor()


    def query(self,sql):
        '''Performing a simple query to the database SQL such as 'SELECT * FROM items' '''
        self.cur.execute(sql)   #Executed the statement
        self.conn.commit()  #Commits the changes to the database
        self.closeDB()  #Closes the database so no further changes can be made without executing a statement

    def getData(self,sql):
        '''Getting the data from the SQL Database'''
        try:
            self.cur.execute(sql)   #Executes the SQL statement
            return self.cur.fetchone()[0]   #Returns the first tuple, this is because SQL returns data in two tuples
                                            # when asked for one item
        except:
            pass

    def closeDB(self):
        self.conn.close()   #Closes the database so no further changes can be made without executing a statement


class itemDB:
    '''Initialises the connection to the database'''
    def __init__(self):

        self.conn = pymysql.connect(host='localhost',
                                    port=3306, user='root',
                                    passwd='', db='smart_mart')

        self.cur = self.conn.cursor()


    def query(self,sql):
        '''Performing a simple query to the database SQL such as 'SELECT * FROM items' '''
        self.cur.execute(sql) #Executed the statement
        self.conn.commit() #Commits the changes to the database
        self.closeDB()  #Closes the database so no further changes can be made without executing a statement


    def getData(self,sql):
        '''Getting the data from the SQL Database'''

        try:
            self.cur.execute(sql)   #Executes the SQL statement
            return self.cur.fetchall()  #Returns all of the data
        except:
            pass

    def getOneData(self,sql):
        try:
            self.cur.execute(sql)   #Executes the SQL statement
            return self.cur.fetchone()[0]   #Returns the first tuple, this is because SQL returns data in two tuples
        except:
            pass



    def closeDB(self):
        self.conn.close()    #Closes the database so no further changes can be made without executing a statement
