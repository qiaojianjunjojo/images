#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
sum=0
def main():
    global sum
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1,5):
                if (i!=k)&(k!=j)&(i!=k):
                    print(i,end='')
                    print(j,end='')
                    print(k)
                    sum+=1
    print("數字個數為:",sum)                                                  
    
if __name__ == '__main__':
    main()
  
