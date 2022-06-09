                                              # Assignment-4 (Python)

#Question 1

marks = float(input("Enter Marks: "))
if marks <= 25:
  print ("F")
elif marks>=25 and marks<45:
  print ("E")
elif marks>=45 and marks<50:
  print ("D")
elif marks>=50 and marks<60:
  print ("C")
elif marks>=60 and marks<80:
  print ("B")
else:
  print ("A")

#Question 2

year = int(input("Type Year: "))
if((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
    print(year, " is a leap year")
else:
	print(year, " is not a leap year")

#Question 3

import random
import math

mark = 0
i = 0
while i in range(10):
    num_1 = random.randint(1,10)
    num_2 = random.randint(1,10)
    question = int(input("Question {} : {} * {} =".format(i+1,num_1,num_2)))
    if question == num_1*num_2:
        print("Your Answer Is Right")
    else:
        print("Your Answer Is Wrong. The Answer Is ", num_1*num_2)
    i = i + 1


#Question 4

candies = -1
while candies <= 200:
    candies = candies + 1
    if candies % 5 == 2:
       if candies % 6 == 3:
          if candies % 7 == 2:
             print(candies, 'candies are in the bowl!')