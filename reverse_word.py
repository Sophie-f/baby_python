def reverse(s):
    new_s = ' '
    j = None
    for i in range(len(s)):
        if s[i] == " ":
            new_s += s[i-1:j:-1] + ' '
            j = i
    new_s += s[i:j:-1]
    return new_s 


print(reverse(input('Enter string ')))
