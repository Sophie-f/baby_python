
def multiplication_table(n):
    my_list=[[]for i in range(n)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            my_list[i-1].append(i*j)
    return my_list          
table = multiplication_table(int(input('Enter number of row ')))
for row in table:
    print(row)    