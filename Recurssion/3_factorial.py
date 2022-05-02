from re import X


# function for recurssion
def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)
    
num = int(input("Enter any number : "))
result = factorial(num)
print("Factorial is : ",result)