                          # Assignment-3 (Python)


#Question 1

number = float(input("Enter the number: "))
a = int(number)
a = bin(a)

frac = str(a)
deci = (number - int(number))
a = deci
frac+= "."
for y in range (7):
    a = a*2
    if (int(a)==1):
        frac+="1"
    a = a-1
else:
 frac+="0"
final=frac.lstrip("-0b")
print(final)

#Question 2

print('Implementing a simple calculator program')
term_math = input('Enter a mathematical expression:')
print("Result :" ,eval(term_math))

#Question 3

import math

                          # Part A

print("a)",(3+4)*(5))

                          # Part B
n = int(input("b) Enter the value : "))
print(n*(n-1)/2)

                          #Part C

rad = float(input("c) Enter the radius : "))
print(4*math.pi*rad**2)

                          #Part D

r = float(input("d) Enter the value: "))
a = int(input("Enter the value of a in degrees: "))
a = (a/ 180)*(math.pi)
b = int(input("Enter the value of b in degrees: "))
b = (b/ 180)*(math.pi)
print(math.sqrt(r*(math.cos(a))**2 + r*(math.sin(b))**2))

                         #Part E

y2 = float(input("Enter the value of y2 : "))
y1 = float(input("Enter the value of y1 : "))
x2 = float(input("Enter the value of x2 : "))
x1 = float(input("Enter the value of x1 : "))
print((y2- y1)/(x2- x1))

#Question 4

#Part A

for y in range(5):
  print(y, end=" ")
print("\n")

#Part B

for p in range (3, 10):
  print(p, end=" ")
print("\n")

#Part C

for t in range (4, 13, 3):
  print(t,end=" ")
print("\n")

#Part D

for h in range (15, 5, -2):
  print(h,end=" ")
print("\n")

#Part E

for j in range (5, 3):
  print(j,end=" ")
print("\n")

#Question 5

c = int(input("Enter the number of carbon : "))
o = int(input("Enter the number of oxygen : "))
h = int(input("Enter the number of hydrogen : "))
m = 1.00794*h + 12.0107*c + 15.9994*o
print("Molecular weight is", m)