class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("My name is "+self.name)
        print("I am {} years old".format(self.age))

        
class student(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.graduateyear=year
    def call(self):
        print("now is {}".format(self.graduateyear))
        
s1=student("Joe",25,2019)

s1.speak()
s1.call()
