#what is function?
#a function is a block of code that runs only when it is called. 

#why we use function??
#1.Avoid repeating code.
#2.makes program clean and organized.
#3.easy to debug and reuse.

#syntax:
#def function_name()
    #code

#example:
def greet():
    print("hello world")
greet()

#function with parameter use to pass values.

def greet(name):
    print(f"Hello{name}")
greet("sakiie")  

def greet(name="abc"):
    print(f"Hello{name}")
greet()

#function with return values:
#used when we want to send result back.
def add(a,b):
    return a+b
result=add(2,3)
print(result)

#task1
#create a function to calculate and return result.
def calc(a,b):
    result=a+b
    return result
op=calc(4,4)
print(op)


#task2
#create a function to check if a num is even or odd.
#use % operator
#frst method
def check_num(num):
    if num %2 ==0:
        return "Even"
    else:
        return "Odd"   
result=check_num(5)
print(result)    

#second method(user input)
def check_num(num):
    if num %2 ==0:
        return "Even"
    else:
        return "Odd" 
n=int(input("Enter a number: "))      
result=check_num(n)
print("The number is: ",result)   

#task3
#create a function to find a factorial of a number.
#use loop or recursion
#input:n=5

number = int(input("Enter a number: "))
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
result = factorial(number)
print(f"The factorial of {number} is {result}.")

#task4
#create a function to find maximum of three numbers.
#use if-else

def find(a,b,c):
    if a>=b and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
x=int(input("Enter a First number: ")) 
y=int(input("Enter a Second number: "))    
z=int(input("Enter a Three number: "))    

result=find(x,y,z)
print("Maximun of three num is: ",result)

#task5
#create a function to check if a string palindrom or not.

#first method
def palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not palindrome"
text=input("Enter a string:")
result=palindrome(text)
print("Result: ",result)    

#second method
def is_palindrome(s):
    s = s.replace(" ", "").lower() 
    #remove spaces and convert to lowercase
    return s == s[::-1] 
    #check if string is equal to its reverse
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")

#task6
#create a function to calculate area of circle.

#first method
def area(r):
    area=3.14*r*r
    return area
radius=float(input("Enter radius: "))
result=area(radius)
print("Area of circle is: ",result)

#second method
import math
def area_of_circle(radius):
    area = math.pi * radius**2
    return area

radius = float(input("Enter the radius of the circle: "))
print("Area of the circle:", area_of_circle(radius))









