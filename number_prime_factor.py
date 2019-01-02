def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True        


def count_factor(num):
    count = 0
    if is_prime(num):
        count = 1
    else:
        for factor in range(2, num//2 + 1):
            if is_prime(factor) and (num % factor == 0):
                count += 1
    return count


n = int(input('Enter the number '))
print(count_factor(n))
