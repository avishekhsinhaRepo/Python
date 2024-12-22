try:
    print(1/0)
except ZeroDivisionError:
    print("An error occurred")
finally:
    print("This will always run")


try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("An error occurred")

x=5
y=0

try:
    z=x/y
except ZeroDivisionError:
    print("An error occurred")
finally:
    print("All done")



def squareInput():
    while True:
        try:
            num = int(input("Enter a number: "))
            print(num**2)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")