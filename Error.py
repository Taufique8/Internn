try:
    a=int(input("Enter your Numberr: "))
    b= 9/a
    print(b)
except Exception as e:
    print(e)
finally:
    print("execution is completed")
    a = [1,2,3,4,5,6,7,8]
for i in a:
    print(i)

a=int(input("Enter your Numberr: "))
b= 9/a
print(b)
a = [1,2,3,4,5,6,7,8]
for i in a:
    print(i)
def myfunction(child1,child2,child3):
    print("the youngest child is: ",child1)
myfunction(child1='amber',child2='taufique',child3='fiza')
def greeting(name):
    print("hell",name)
'''import pandas as pd
a = {"Name":["Fiza","Taufique","Amber"],
     "Age":[19,18,18],
     "Gender":["Female","Male","Male"]}
df = pd.DataFrame(a,index=["user1","user2","user3"])

print(df.loc["user2"])'''





