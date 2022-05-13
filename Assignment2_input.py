                                    #Assignment-2 (Python)

#Question 1

#Part (A)

input_string = "Python is a case sensitive language"
print(len(input_string))

#Part (B)

input_string = "Python is a case sensitive language"
print(input_string[::-1])

#Part (C)

input_string = "Python is a case sensitive language"
print(input_string[10:27])

#Part(D)

input_string = "Python is a case sensitive language"
print(input_string.replace("a case sensitive", "object oriented"))

#Part(E)

input_string = "Python is a case sensitive language"
print(input_string.find("a"))

#Part(F)

input_string = " Python is a case sensitive language "
print(input_string.replace(" ",""))

#Question 2

Name = input("Enter your name")
S = int(input("Enter your SID"))
Department_Name = input("Enter you Department")
CG = float(input("Enter you cg"))

print("Hey, %s Here!"%(Name),"\n"
      "My SID is %d"%(S),"\n"
      "I am from %s" %(Department_Name), "and my CGPA is %f"%(CG))

#Question 3

#Part(A)

a=56
b=10
print(a&b)

#Part(B)

a=56
b=10
print(a|b)

#Part(C)

a=56
b=10
print(a^b)

#Part(D)

a=56
b=10
print(a<<2, "\n", b<<2)

#Part(E)

a=56
b=10
print(a>>2,"\n",b>>4)

#Question 4

a=str(input("Enter your string"))
b=a.find("name")

if b == -1:
      print("No")
else:
      print("Yes")

#Question 5

Side1 = float(input("Enter length 1 ="))
Side2 = float(input("Enter length 2 ="))
Side3 = float(input("Enter length 3 ="))

Side_1 = int(Side1)
Side_2 = int(Side2)
Side_3 = int(Side3)

a = Side_1 + Side_2
b = Side_2 + Side_3
c = Side_1 + Side_3

Check_1 = a>Side_3
Check_2 = b>Side_1
Check_3 = c>Side_2

answer = str(Check_1 and Check_2 and Check_3)
answer = answer.replace("True","Yes")
answer = answer.replace("False","No")
print(answer)

#Question 6

Number1 = int(input("Enter your first number ="))
Number2 = int(input("Enter your second number ="))

A = Number1^Number2

B =bin(A)
Check_string = str(B)

C = Check_string.count("1")

print(C)
print(Check_string)



