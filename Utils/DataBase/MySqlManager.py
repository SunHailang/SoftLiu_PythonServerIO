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
    

    
if __name__ == "__main__":
    sql = MySqlManager("10.192.91.40", "root", "hlsun123", "hlsun")
    data = sql.SelectData("select * from student where isDelete=1;")
    print(data[0], len(data))
    count = sql.GetCount("select count(*) from student;")
    print(count)

