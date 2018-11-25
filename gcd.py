def calculate_gcd(a, b):#recursive version (روش نردبانی ب م م)
    if a > b:  #b is always bigger
        a,b = b,a
    if a == 0:
        return b    
    return calculate_gcd(a, b%a)