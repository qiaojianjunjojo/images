from multiprocessing import Process,Lock
from time import sleep

counter = [0]
lock =Lock()


def sub_task1(string,counter):
    while counter[0] < 10:
        lock.acquire()
        print(string, end='', flush=True)
        counter[0] += 1
        lock.release()
        sleep(0.01)

def sub_task2(string,counter):
    while counter[0] < 10:
        lock.acquire()
        print(string, end='', flush=True)
        counter[0] += 1
        
        lock.release()
        sleep(0.01)
        
def main():
    Process(target=sub_task1, args=('Ping', counter)).start()
    Process(target=sub_task2, args=('Pong', counter)).start()


if __name__ == '__main__':
    main()