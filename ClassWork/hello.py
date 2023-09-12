# print('Hello World')

# var = "World"
# print(f"Hello {var}")

# print("Hello {}".format('World'))

# print("Hello %s"%("World"))

# print("Hello",end=" World")

# a = str(input("Input a: "))
# b = str(input("Input b: "))

# if len(a)<4 and len(b)<4:
#     print(int(a)+int(b))
# else:
#     print("Limit Exceeded")

import random
# print(random.randint(1,10))

arr = ['+','-','*','/','%']

eq = str(random.randint(1,99)) + str(arr[random.randint(0,4)]) + str(random.randint(1,99))

print(eq)
# print(eval(eq))

inp = int(input("Enter your equation: "))

if eval(eq) == inp:
    print("Correct!")
else:
    print("Wrong!")