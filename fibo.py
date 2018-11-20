def fibo(n):
    if n <2:
        return n
    else:  
        return fibo(n-1)+fibo(n-2)    
m = int(input("Enter number "))    
result = map(fibo,range(1,m+1))
for num in result:
    print(num)