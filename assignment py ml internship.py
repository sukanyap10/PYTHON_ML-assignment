#Q1 
x=int(input("enter num1"))
y=int(input("enter num2"))
r=x+y
print(x+y)

#Q2
n=int(input())
if n%2==0:
    print('even')
else:
    print("odd")

#Q3
n=int(input("enter any no"))
fac=1
i=1
while i<=n:
    fac=fac*i
    i=i+1
print("Factorial of the number is :",fac)

#Q4
name=input("enter your name")
print("Hello",name,"welcome to the site !")

#Q5
user_input = input("Please enter the text you want to write to the file: ")
file=open('new.txt','w')
file.write(user_input)
f.close()
print("The text file is created successfully")

#Q6
f=open('new.txt','r')
content = f.read()
print(content)

#Q7
str=input('enter any string')
print(len(str))

#Q8
str1=input("enter first string")
str2=input("enter second string ")
r =  str1 + str2
print(r)

#Q9
str=input('enter any string')
sub=input('enter any substring')
if sub in str:
    print('substring is present')
else:
    print('substring is not present')

#Q10
s=input("enter")
print(s.upper())

#Q11
n=int(input("enter the no of terms to generate "))
sec=0
l=1
print(sec)
print(l)
c=2
while c<=n:
    next = sec +l
    print(next)
    sec=l
    l=next
    c=c+1

#Q12
number = input("Enter a number: ")
number = abs(int(number))
number_str = str(number)
digit_sum = 0
for digit in number_str:
    digit_sum += int(digit)
print(f"The sum of the digits is: {digit_sum}")

#Q13
byear=int(input("enter your birth year"))
pyear=2024
age= pyear-byear
print("age of user is :",age)

#Q14
lines = []
print("Enter multiple lines of input (press Enter on an empty line to finish):")
while True:  
    line = input()   
    if line == "":      
        break 
    lines.append(line)
print("\nYou entered:")
for line in lines:
    print(line)


#Q15
import csv

file_name = input("Enter the CSV file name: ")

try:
    with open(file_name, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
    print("CSV data printed successfully!")
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
except Exception as e:
    print("An error occurred:", e)


#Q16
str=input('enter any string')
c=0
for i in str:
    c=c+1
    print("The occurence of" ,i ,"= ",c)

#Q17
str=input('enter any string')
new_str =str.title()
print("Title case string is :",new_str)

#Q18
s1=input("enter first string")
s2=input("enter second string")
s1= s1.replace(" ","").lower()
s2= s2.replace(" ","").lower()
if sorted(s1) == sorted(s2):
    print("the two strings are anagrams")
else:
    print("they are not anagrams")

#Q19
str=input("enter any string")
punc= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
new=""
for i in str:
    if i not in punc:
        new= new+ i
print("String without punctuation:",new)

#Q20
l=[1,2,3,4]
s=0
for i in l:
    s=s+i
print(s)
    
#Q21
elements = input("Enter a list of elements separated by spaces: ").split()
target = input("Enter the element to count: ")
count = elements.count(target)
print(f"The element '{target}' occurs {count} times in the list.")

#Q22
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
minimum = min(numbers)
maximum = max(numbers)
print(f"The minimum value is: {minimum}")
print(f"The maximum value is: {maximum}")

#Q23
d = input("Enter 'c' to convert Celsius to Fahrenheit or 'f' to convert Fahrenheit to Celsius: ")
if d == 'c':
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"{c} Celsius is equal to {f} Fahrenheit.")
elif d == 'f':
    f = float(input("Enter temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print(f"{f} Fahrenheit is equal to {c} Celsius.")
else:
    print("Invalid input! Please enter 'c' or 'f'.")

#Q24
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operator"
print(f"The result of {num1} {operator} {num2} is: {result}")

#Q25
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file, 'r') as source, open(destination_file, 'w') as destination:
        destination.write(source.read())
    print("Contents copied successfully!")
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
except Exception as e:
    print("An error occurred:", e)

#Q26
string = input("Enter a string: ")
prefix = input("Enter the prefix: ")
suffix = input("Enter the suffix: ")
s1 = string.startswith(prefix)
e1 = string.endswith(suffix)
print(f"The string '{string}' starts with the prefix '{prefix}': {s1}")
print(f"The string '{string}' ends with the suffix '{suffix}': {e1}")

#Q27
str=input('enter string')
char=list(str)
print("list of characters :",char)


