# # give List of string with 20 elements
# names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'John', 'Kincaid', 'Larry', 'Mehul', 'Nancy', 'Oscar', 'Patton', 'Quincy', 'Ray', 'Sally', 'Tom']
# def startsWithA(name):
#     if name[0] == 'A':
#         return name
# def filterNones(name):
#     if name != None:
#         return name
#
# for name in filter(None,map(startsWithA, names)):
#     print(name)



# #list of numbers
# nums = [1,2,3,4,5,6,7,8,9,10]
#
# def isEven(num):
#     if num % 2 == 0:
#         return num
#
# for num in filter(lambda  num : num%2 ==0, nums):
#     print(num)


message= "This is global variable"

def greet():
    global message
    message = "This is enclosed variable"

greet()
print(message)