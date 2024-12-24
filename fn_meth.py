import string


## Volume of Cube

def volume_cube(radius):
    return (4/3)*3.14*radius**3


print(volume_cube(2))


## Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    if num in range(low,high+1):
        return True
    else:
        return False

ran_check(5,2,7)


## Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(s):
    lower = 0
    upper = 0
    for str in s:
        if str.islower():
            lower += 1
        elif str.isupper():
            upper += 1
        else:
            pass
    print("Original String : ", s)
    print("No of Upper case characters : ", upper)
    print("No of Lower case characters : ", lower)

up_low("Hello Mr. Rogers, how are you this fine Tuesday?")



##Write a Python function that takes a list and returns a new list with unique elements of the first list

def unique_list(lst):
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

# Write a Python function to multiply all the numbers in a list.


def multiply_list_nums(list_of_nums):
    result = 1
    for num in list_of_nums:
        result *= num
    return result

print(multiply_list_nums([1,2,3,-4]))

#Write a Python function that checks whether a word or phrase is palindrome or not


def palindrome(s):
    s = s.replace(' ','')
    return s == s[::-1]

def ispangram(str1, alphabet=string.ascii_lowercase):
    list_of_alphabet = list(alphabet)
    for s in str1:
        if s in list_of_alphabet:
            list_of_alphabet.remove(s)
            print(list_of_alphabet)
    return len(list_of_alphabet) == 0


print("ispangram",ispangram("The "))