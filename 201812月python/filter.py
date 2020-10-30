l =[x for x in  range(1,11)]
res = filter(lambda x :x%2==0,l)
print(res)
res = [x for x in res]
print(res)

l =[x for x in  range(1,11) if not x%2]
print(l)
