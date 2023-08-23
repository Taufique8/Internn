''' List in python
a = [ 5,1,2,40,3,20.5]
print(a)
print(type(a))
a.append('Reshmi')
print(a)
a.copy()
print(a)
print(a.count(3))
print()
a.extend(a)
print(a)
print(a.index('amber'))
print(a.insert(40,0))
print(a.pop())
a.insert(0,'ayesha')
a.remove(True)
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.clear()
print(a)

#tuple in python

a = (2,3,4,'fiza','amber',2,True)
print(a)
print(type(a))
print(a.count(2))
print(a.index('fiza'))

#set in python

a = {2,3,4,'fiza','saniya',20.5,True}
b = {4, 3, 2,'amber','ayesha','fiza',20.5}
print(a)
print(b)
print(type(b))
a.add(20)

print(a.difference(b))
a.discard('amber')
print(a)
print(b.intersection(a))
print(a.intersection_update(b))
#a.isdisjoint ()
print(a.issubset(b))
print(b.issuperset(a))
print(b.symmetric_difference(a))
a.symmetric_difference_update(b)
print(a.union(b))
print(a|b)
a.update(b)
print(a)
a.update

# Dictionary in python

a = {'name':'Taufique','company':'Google',4:'data scientist'}
print(a)
print(type(a))
#a.fromkeys('name')
print(a.get('n'))
print(a.items())
print(a.keys())
print(a.pop('name'))
print(a.setdefault('naam','Fiza'))
print(a.get('naam'))
print(a)
#a.update('saniya')
print(a.values()) 

# funnction in python

def amber(name):
    print('fiza')

amber('Taufique')

# class in python

class amber():
    def greet(self,name):
        print('Hi,',name)
    def add(self,a,b):
        print(int(a+b))
class fiza(amber):
    def hm(self):
        print('ws')
class saniya(amber):
    def gm(self):
        print('Good Morning')

class const:
    def __init__ (self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(f"My Name is {name}, im {age} year old, I belong from {address}")
a = const('Fiza',19,'darbhanga')'''












