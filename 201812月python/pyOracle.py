#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import cx_Oracle
import pandas as pd
"""
  connet to Oracle
  
  帶變量SQL例子：
  sql = "SELECT * from wip_code where code_cate='%s' and code='%s' "%(code_cate, condit)
"""
class connectToOracle():
 
    def __init__(self,usrName=None, password=None, IP=None, port=1521, dbName=None):
        self.connectObj = ""
        self.connCnt = 0
        self.cursorCnt = 0
        self.sqlList = []
        self.usrName = usrName
        self.password = password
        self.IP = IP
        self.port =port 
        self.dbName = dbName
        
#  數據庫連接          
    def initOracleConnect(self):
        try:
            oracle_tns = cx_Oracle.makedsn(self.IP, 1521,self.dbName)
            if self.connCnt == 0:
                self.connectObj = cx_Oracle.connect(self.usrName, self.password, oracle_tns)
                self.connCnt += 1
        except  :
            print('connect to DB fail')
            
#  取得數據庫連接  
    def getOracleConnect(self):
        self.initOracleConnect()
        return self.connectObj
    
# 斷開數據庫連接    
    def closeOracleConnect(self, connectObj):
        connectObj.close()
        self.connCnt -= 1
        
# 獲取光標
    def getOracleCursor(self):
        self.initOracleConnect()
        self.cursorCnt += 1
        return self.connectObj.cursor()

# 關閉光標    
    def closeOracleCursor(self, cursorObj):
        cursorObj.close()
        self.cursorCnt -= 1
        if self.cursorCnt == 0:
            self.closeOracleConnect(self.connectObj)

# 1.方式一 搜索數據 返回dataframe
    def sqlSelect(self, sql):
        selectCursor = self.getOracleCursor()
        selectCursor.execute(sql)
        rs = selectCursor.fetchall()
        result = pd.DataFrame(rs)
        self.closeOracleCursor(selectCursor)
        return result
 
# 
# 1.方式二 搜索數據  返回dataframe
    def sqlPdSelect(self, sql):
        connectObj = self.getOracleConnect()
        result = pd.read_sql(sql,connectObj)
        self.closeOracleCursor(selectCursor)
        return result
    
#  update insert delete 數據  并且commit
    def sqlExecute(self,sql):
        selectCursor = self.getOracleCursor()
        selectCursor.execute(sql)
        self.getOracleConnect().commit()
        self.closeOracleCursor(selectCursor)
        
#  將要執行的sql到存到列表中   
    def addExecuteSQL(self,sql):
        return self.sqlList.append(sql)
# 執行sql列表中的sql，並一起commit    
    def allSqlExecute(self):
        selectCursor = self.getOracleCursor()
        if len(self.sqlList)==0:
            return print('No sql execute')
 
        for sql in self.sqlList:
            selectCursor.execute(sql)
        self.getOracleConnect().commit()
        self.sqlList =[]
        self.closeOracleCursor(selectCursor)
        

