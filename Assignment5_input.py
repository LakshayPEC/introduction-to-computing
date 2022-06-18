                                           # Assignment-5 (Python)

#Question 1

a = input("Enter the string:")

str = ""
for i in a:
    str = i + str
print("The reversed string is:", str)

#Question 2

a = int(input("Enter the lower range:"))
b = int(input("Enter the upper range:"))
c = int(input("Enter the number:"))

for i in range(a,b+1):
    if i%c == 0:
        print(i,"is divisble by",c)

#Question 3

import math
a = float(input('Enter the length of first side: '))
b = float(input('Enter  the length of second side: '))
c = float(input('Enter  the length of third side: '))

if a+b>c and b+c>a and a+c>b:
   s = (a + b + c) / 2
   Area = math.sqrt(s*(s-a)*(s-b)*(s-c))
   print('The area of the triangle is %0.2f' %Area)

else:
    print("The traingle is not possible")

#Question 4

n=5;
for i in range(n):
    for j in range(i):
        print ('* ', end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')

#Question 5

n = int(input("Enter the number of rows: "))
value = 65
for i in range(0,n+1):
    for j in range(0,i):
        ch = chr(value)
        print(ch, end=" ")
        value = value + 1
        if(value>90):
            value=65
    print()

#Question 6

Lower_value = int(input("Enter the lower range value: "))
Upper_value = int(input("Enter the upper range value: "))

print("The prime numbers in the range are: ")
for number in range(Lower_value, Upper_value + 1):
    if number > 1:
        for i in range (2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
print("\n")

#Question 7

for i in range(1,501):
    if (i%7 == 0) and (i%11 == 0):
        print(i)
    else:
        continue

#Question 8

lst = []
n = 10

for i in range (0,n):
    ele = int(input ("Enter The Number: "))
    lst.append(ele)

#a) postive numbers

print("Positive numbers in", lst, "are: ")
for i in lst:
    if i >= 0:
       print (i, end = " ")

#b) negative numbers
print("\nNegative numbers in", lst, "are: ")
for i in lst:
    if i <= 0:
       print (i, end= " ")

#c) odd numbers
print ("\nodd numbers in", lst, "are: ")
for i in lst:
    if i%2 != 0:
       print (i, end=" ")

#d) even numbers
print("\nEven numbers in", lst, "are: ")
for i in lst:
    if i%2== 0:
        print (i, end = " ")

#e) Number of times each number occurs in the List
for i in lst:
    g=0
    n=0
    if (i=="----"):
        continue

    for j in lst:
        if(i==j):
            n=n+1
            lst [g]='----'
        g=g+1
    print("\n", i," occured ",n," times")

#Question 9

user_list = input("Enter the list of words seperated by comma(,):")

word_list = user_list.split(",")

counts = dict()

for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)

