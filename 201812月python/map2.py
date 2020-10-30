l = [1,2,3,4,5]
result1 = map(lambda x :x**2,l)
print(result1)
result = [x for x in result1 if x > 10]
print(result)
