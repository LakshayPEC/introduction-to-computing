                                                # Assignment-6 (Python)

'''Question 1'''

a = int(input('Enter A Number: '))
List = []
if a > 0:
  for i in range (1,a):
   b = a%i
   if b == 0:
     List.append(i)
     sum(List)
  if sum(List) == a:
    print('It is a Perfect Number')
  else :
    print('It is not a Perfect Number')
else :
  print('Enter a Positive Number')

'''Question 2'''

a = str(input('Enter a String: '))
a_inv = a[::-1]
if a == a_inv:
  print("The Word Is A Palindrome")
else:
  print("The Word Is Not A Palindrome")

'''Question 3'''

n=int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()

'''Question 4'''

def check_pangram(arg):
  if len(set('abcdefghijklmnopqrstuvwxyz') - set(arg.lower())) == 0:
    return True

  return False

user_str = input("Enter a string to check for pangram : ")

if(check_pangram(user_str)):
  print("It is a pangram string")
else:
  print("Not a pangram string")

'''Question 5'''

n=input("enter the string: ")
l=n.split('-')
l.sort()
print('-'.join(l))

'''Question 6'''

def student_id(*args):
   if type(args[0]) == int:
     print("The student id is", args[0])
   elif type(args[0])==str and type(args[1])==int:
     print("The student name is ", args[0])
     print("The student class is ", args[1])


id_input = int(input("Please enter the student id: "))
name_input = str(input("Please enter the student name: "))
class_input = int(input("Please enter the student class: "))


student_id(id_input)
student_id(name_input, class_input)

'''Question 7'''

class Student:
    pass
class Marks:
    pass
student1 = Student()
marks1 = Marks()
print(isinstance(student1, Student))
print(isinstance(marks1, Student))
print(isinstance(marks1, Marks))
print(isinstance(student1, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))

'''Question 8'''

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result
print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

'''Question 9'''

class validity:

    def f(str):

        a= ['()', '{}', '[]']

        while any(i in str for i in a):

            for j in a:

                str = str.replace(j, '')

        return not str

s = input("enter : ")

print(s, "-", "is balanced"

      if validity.f(s) else "is Unbalanced")