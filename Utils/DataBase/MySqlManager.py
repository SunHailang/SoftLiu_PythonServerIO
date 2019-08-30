import pymysql

class MySqlManager (object) :

    def __init__(self, host, user, pw, database):
        print("Name: ", user, ", Password: ", pw)
        self.hostName = host
        self.userName = user
        self.passWord = pw
        self.databaseName = database

    def __del__(self):
        print("MySql Del.")

    def SelectData(self, sql):
        db = pymysql.connect(self.hostName, self.userName, self.passWord, self.databaseName)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        db.close()
        return data

    def GetCount(self, sql):
        db = pymysql.connect(self.hostName, self.userName, self.passWord, self.databaseName)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()        
        cursor.close()
        db.close()
        return data
    

    


