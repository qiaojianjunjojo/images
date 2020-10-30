# map fucntion example
#Python函数编程中的map()函数是将func作用于seq中的每一个元素，
#并将所有的调用的结果作为一个list返回
import time
st=time.time()
for n in range(2,6):#位數
    print("{}位數的水仙花數為：".format(n))
    for num in range(10**(n-1),10**(n)):      
        count=0
        if sum(map(lambda x:int(x)**n,str(num)))==num:          
            print(num)
            count+=1
     
        
et=time.time()
print("It cost {}s".format(et-st))
