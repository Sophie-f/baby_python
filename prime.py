def is_prime(n):
    if n == 1 or n == 0:    
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True


count = 0
for i in range(1, 100):
    if is_prime(i):
        print(i)
        count = count+1
print(count)
