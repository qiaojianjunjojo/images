import pymysql

def main():
    dept_no = int(input("請輸入需要刪除的部門編號："))
    con = pymysql.connect(host='localhost',port = 3333,database = 'hrs',
                         charset = 'utf8',user = 'root',password = '123456',autocommit = 'True')

    try:
        with con.cursor() as cursor:
            sql = 'delete from tb_dept where dno = {}'.format(dept_no)
            result = cursor.execute(sql)
            if result == 1:
                print('刪除成功')
            #on.commit()
    finally:
        con.close()

if __name__ == '__main__':
    main()
        
        
