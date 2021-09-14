def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if (a==0 and b==0):
        raise ValueError("undefined")
    elif b==0:
        raise ValueError("we cannot divide")
    return a/b



#x=float(input("Enetr first value:"))
#y=float(input("Enter second value:"))
#print("add = ",add(x,y),"\n","Sub = ",sub(x,y),"\n","Mul = ",mul(x,y),"\n","div = ",div(x,y))




