def sum(n):
    # rem=0
    if n < 10:
        return n
    else:
        # rem = rem+(n%10)
        return n%10+sum(n//10)
    
num = int(input("Enter the number : "))
print("sum = ",sum(num))