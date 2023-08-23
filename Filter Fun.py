#filter function
num = [2,4,6]
multi = filter(lambda a: a % 2==0 , num)
print(list(multi))
num = [2,4,5,6]
def iseven(n):
    return n % 2==0
result = filter(iseven,num)
print(list(result))
# map function
multi = map(lambda a: a*2 , num)
print(list(multi))
#import reduce function
from functools import reduce
num = [
    ('care',2),('airoplane',6)
    ]
amber = reduce(lambda a,b: a[1]+b[1],num)
print(amber)
#print(help(append))
    






