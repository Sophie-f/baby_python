def lcm(a, b):
    for i in range(1, b+1):
        result = a * i
        if result % b == 0:
            return a * i


m = int(input('Enter first number '))
n = int(input('Enter second number '))
print(lcm(m, n))
