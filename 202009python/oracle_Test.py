# -*- coding:utf-8 -*-
import cx_Oracle

class Oracle(object):
    def __init__(self,userName,password,host,instance):
        self._conn = cx_Oracle.connect("%s/%s@%s/%s" % (userName,password,host,instance))
        self.cursor = self._conn.cursor()


    def queryAll(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def queryOne(self,sql):
         self.cursor.excute(sql)
         return self.cursor.fetchone()
        
    def queryBy(self,sql,nameParams={}):
        if len(nameParams) > 0 :
            self.cursor.execute(sql,nameParams)
        else:
            self.cursor.execute(sql)

        return self.cursor.fetchall()
    
        #update  method
    def updateBy(self,sql,params={}):
        self.cursor.prepare(sql)
        self.cursor.execute(sql,params)
        self.commit()
        
        #insert method
    def insertBy(self):
        pass

    def insertBatch(self,sql,nameParams=[]):
        self.cursor.prepare(sql)
        self.cursor.executemany(None, nameParams)
        self.commit()
        
            #insert,update,delete --commit    
    def commit(self):
        self._conn.commit()
        
        # 析构~~
    def __del__(self):
        if hasattr(self,'cursor'):
            self.cursor.close()
            print('python解析器自動關閉cursor')
            
        if hasattr(self,'_conn'):
            self._conn.close()
            print('python解析器自動關閉_conn')


def main():
    oracle = Oracle('PSCMAPPDA1','PSCMAPPDA1','10.189.128.47','fswappdb1')
    sql = """
        select 1 from dual
    """
    rs = oracle.queryAll(sql)
    print(rs)
            
if __name__ == '__main__':
    main()

