def perfect(n):
    count = 0
    for i in range(1,n):
        if n % i == 0:
            count = count + i
    if count ==n :
        return True
    else:
        return False


print(perfect(int(input('enter number \n'))))        