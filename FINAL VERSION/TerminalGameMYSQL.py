#https://github.com/PyMySQL/PyMySQL for package

import pymysql.cursors
import datetime

FakeAnwser = True

class PlayersInformation:
    def __init__(self):
        self.UID = 0
        self.PlayerAmount = 0
        self.Hint = ""
        self.Language = 0
        self.LastMessage = ""
        self.DateAndTime = "2000-10-02 01:03:46"
Pinfo = PlayersInformation()
TEMPinfo = PlayersInformation()

f =  '%Y-%m-%d %H:%M:%S'

def GetLastData():

    connection = pymysql.connect(host='localhost',
                                 user='pi',
                                 password='test123',
                                 db='hackgame',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    with connection.cursor() as cursor:
        sql =  sql = "SELECT `uid`, `players`, `language`,`Message`,`DateAndTime`  FROM `GameInformation`" #GameInformation
        cursor.execute(sql)
        result = cursor.fetchall()#fetchone()        
        connection.close()
        
    return result


def IndexData():

    global FakeAnwser
    global Pinfo
    global TEMPinfo

    FakeAnwser = True

    if FakeAnwser == True:
        TEMPinfo.UID = 999
        TEMPinfo.PlayerAmount = 4
        TEMPinfo.Language = 0
        TEMPinfo.LastMessage = ""
        TEMPinfo.DateAndTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Pinfo = TEMPinfo
        return Pinfo
    else:
        results = GetLastData()
        highestUID = 0
        updateData = False     
        newtime = datetime.datetime

        for rows in results: 
            for data in rows:
                if data == "uid":
                    TEMPinfo.UID = rows['uid']
                if data == "players":
                    TEMPinfo.PlayerAmount = rows['players']
                if data == "language":
                    TEMPinfo.Language = rows['language']
                if data == "Message":
                    TEMPinfo.LastMessage = rows['Message']
                if data == "DateAndTime":
                    TEMPinfo.DateAndTime = datetime.datetime.strptime(str(rows['DateAndTime']), f)
                if TEMPinfo.UID >= Pinfo.UID:         
                    updateData = True
           
            if updateData == True:
                Pinfo = TEMPinfo

        return Pinfo




    