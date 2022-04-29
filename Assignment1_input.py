#Assignment-1 (Python)

'''Question No.1 (This python program is used to
find average of three numbers entered by the user.)'''

a=(int(input("enter your first no:")))
b=(int(input("enter your second no:")))
c=(int(input("enter your third no:")))
avg=(a+b+c)/3
print("Average of the three no. is", avg)

'''Question No.2 (This python program
 is used to compute a person's income tax.)'''

var1=(int(input("enter your gross income:")))
var2=(int(input("enter the no. of dependent")))
TI=(var1-10000-var2*3000)
print("Taxable income is",TI)
TR=20/100
T=TI*TR
print('person\'s income tax is',T)

'''Question No.3'''

S=(int(input("enter your SID")))
N=(str(input("enter your Name")))
G=(str(input("enter your gender")))
C=(str(input("enter your Course Name")))
P=(float(input("enter your CGPA")))
L=[S, N, G, C, P]
print(L)

'''Question No.4'''

S1=(int(input("enter your marks")))
S2=(int(input("enter your marks")))
S3=(int(input("enter your marks")))
S4=(int(input("enter your marks")))
S5=(int(input("enter your marks")))
Marks=[S1,S2,S3,S4,S5]
Marks.sort()
print(Marks)

'''Question No.5'''

#Part a

C=["Red", "Green", "White", "Black", "Pink", "Yellow"]
C.remove("Black")
print(C)

#Part b

L=["Red", "Green", "White", "Black", "Pink", "Yellow"]
L[3:5]=["Purple"]
print(L)