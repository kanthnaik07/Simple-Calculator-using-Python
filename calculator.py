def add(x,y) :
    return x + y

def substract(x,y) :
    return x - y

def multiply(x,y) :
    return x * y 

def divide(x,y) :
    return x/y

def power(x,y) :
    return pow (x,y)

def sqrt(x) :
    return sqrt (x), x>0
    
def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)
        
def log(x) :
    import math
    return math.log(x,(10))
    
# take input from user
print("Select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.power")
print("6.sqrt")
print("7.factorial")
print("8.log")
choice=input("Enter choice 1/2/3/4/5/6/7/8/:")
num1=int(input("Enter first number: "))
num2=int(input("Enter the second number: "))

if choice == '1':
   print(num1, "+", num2,"=", add(num1,num2))

elif choice == '2':
   print(num1, "-", num2,"=", substract(num1,num2))

elif choice == '3':
   print(num1, "*", num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1, "/", num2,"=", divide(num1,num2))

elif choice == '5':
   print(num1, "^", num2,"=", power(num1,num2))
 
elif choice == '6':
   sqrt = num2 ** 0.5
   if num2 < 0:
     print("square root doesn't exist")
   print("square root", num2,"=", sqrt)
   
elif choice == '7':
   if num1 < 0:
    print("Factorial cannot be found for negative numbers")
   if num1 == 0:
    print("Factorial of 0 is 1")
   else:
    print("Factorial of", num1, "is: ", factorial(num1))

elif choice == '8':
   if num1 == 1:
     print("log of 1 is 0")
   if num1 == 10:
     print("log of 10 is 1")
   else:
     print("log of", num1 , "is: " , log(num1))
   if num1 < 0:
     print("log cannot be found for negative number")
   if num1 == 0: 
     print("log of 0 is not defined")

   
else: 
    print("Invalid input")