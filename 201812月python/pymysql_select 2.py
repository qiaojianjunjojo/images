import pymysql

'''
select不需要設置autocomiit為True
fetchall()
'''

from pymysql.cursors import DictCursor


def main():
    con = pymysql.connect(host='10.189.143.130', port=3333,
                          database='hrs', charset='utf8',
                          user='root', password='123456')
    try:
        with con.cursor(cursor=DictCursor) as cursor:
            cursor.execute('select dno as no, dname as name, dloc as loc from tb_dept')
            results = cursor.fetchall()
            print(results)
            print('编号\t名称\t所在地')
            for dept in results:
                print(dept['no'], end='\t')
                print(dept['name'], end='\t')
                print(dept['loc'])
    finally:
        con.close()


if __name__ == '__main__':
    main()


        
        
