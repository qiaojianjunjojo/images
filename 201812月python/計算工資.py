"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta,abstractmethod
class Work(object):
    def __init__(self,name):
        self._name=name
    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        '''
        获得月薪
        '''
        pass

class Manager(Work):
    def get_salary(self):
        return 15000.0

class Programmer(Work):
    def __init__(self,name,hour=0):
        super().__init__(name)
        self._hour=hour
        
    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self,hour):
        self._hour = hour if hour >0 else 0

    def get_salary(self):
        return 150.0 * self._hour

class Saleman(Work):
    def __init__(self,name,amount=0):
        super().__init__(name)
        self._amount=amount
        
    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self,amount):
        self._amount = amount if amount>0 else 0

    def get_salary(self):
        return 1200.0 + self._amount * 0.05

def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Saleman('荀彧'),
        Saleman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = int(input('请输入%s本月工作时间: ' % emp.name))
        elif isinstance(emp, Saleman):
            emp.sales = float(input('请输入%s本月销售额: ' % emp.name))
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
    
