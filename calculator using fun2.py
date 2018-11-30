def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y



A= float(input("Enter First value: "))
B= float(input("Enter second value: "))
cal= input("Enter your arithmetic operator: ")

if cal == "add" or cal == "ADD" or cal== "Add":
       print(add(A,B))
elif cal == "sub" or cal=="Subrtact" or cal== "Sub" or cal== "subtract":
    print(sub(A,B))
elif cal == "div" or cal=="Divide" or cal=="divide" or cal== "Div" :
    print(div(A,B))
elif cal == "mul" or cal== "multiplication" or cal=="Multiplication" or cal=="Mul":
        print(mul(A,B))
else:
     print("Selection is not made")