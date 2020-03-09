#we need to import sys library to reconfigure the recursion limit
import sys as system
from math import e,log,floor

#we need our recursive function to work at least 2000 times so we can go for 3000 recursion limit
system.setrecursionlimit(3000)

#the function below saves (1/2)^n in another format:
# so every item of the list is a list itself that the first index of it is like a mantissa of the result 
# and the second number is the power of 10 (something like e in IEEE standard) 
def NumConvertor(n):
    if n==0:
        return [1,0]
    if n==1:
        return [5,1]
    temp = NumConvertor(n-1)
   
    temp[0]*=5
    temp[1]+=1
    if temp[0]>=10:
        temp[0]=temp[0]/10
        temp[1]-=1
    return temp

#because our numbers are stored in a list we need to define an alternate version of nepperian logarithm that works on list
def altNepperianLog(L):
    return log(L[0],e)-L[1]*log(10,e)    

#so as we need an alternate version of divide
def altDivide(a,b):


    if a[1]==b[1]:
        return [a[0]/b[0],0]
    elif a[1]<b[1]:
        return [a[0]/b[0],b[1]-a[1]]
    else:
        return [a[0]/b[0],a[1]-b[1]]    


def Pfinder(func,n):

    x3=func(n+1) 
    x2=func(n)
    x1=func(n-1)
    p = altNepperianLog(altDivide(x3,x2))/altNepperianLog(altDivide(x2,x1))
    return p        


#p is not round because of the divison proximity
n =int(input("\n\n\nPlease input number :>>> "))
print("\n\n")
for i in range(1,n+1): 
    print(i,">>> P:",Pfinder(NumConvertor,i))    