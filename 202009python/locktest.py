import cx_Oracle
import threading
import time
# Create a Connection Pool
lock = threading.Lock()
pool = cx_Oracle.connect("LCDWINT",
        "LCDWINT123", "10.189.128.64:1521/phain", threaded=True)


def TheLongQuery(info):
    # global lock
    # lock.acquire()
    try:
        print(f"{info}:start!")  
        cursor = pool.cursor()
        cursor.arraysize = 25000
        cursor.execute("""
        SELECT * FROM BEOLCT2_V ORDER BY GRADE
                """)
        while True:
            rows = cursor.fetchall()
            if not rows:
                break
        print(f"{info}:end!")
            
    except Exception as e:
        print(str(e))
    finally:
        # lock.release()
        pass

def DoALock():
    with pool.acquire() as conn:
        cursor = conn.cursor()
        print("DoALock(): beginning execute...")
        cursor.callproc(sleepProcName, (5,))
        print("DoALock(): done execute...")


thread1 = threading.Thread(None, TheLongQuery,args=("1号",))
thread1.start()

thread2 = threading.Thread(None, TheLongQuery,args=("2号",))
thread2.start()

thread3 = threading.Thread(None, TheLongQuery,args=("3号",))
thread3.start()

thread4 = threading.Thread(None, TheLongQuery,args=("4号",))
thread4.start()

thread5 = threading.Thread(None, TheLongQuery,args=("5号",))
thread5.start()

thread6 = threading.Thread(None, TheLongQuery,args=("6号",))
thread6.start()

thread7 = threading.Thread(None, TheLongQuery,args=("7号",))
thread7.start()

thread8 = threading.Thread(None, TheLongQuery,args=("8号",))
thread8.start()


thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()

print("All done!")