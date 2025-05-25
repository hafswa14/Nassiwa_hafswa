def calculate_factorial(n):
    fact = 1
    for x in range(1,n+1):
        fact *=x 
    return fact

print(calculate_factorial(5))

       