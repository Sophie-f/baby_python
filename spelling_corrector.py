def single_insert_or_delete(s1,s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if s1 == s2:
        return 0    
    if len(s1) > len(s2):
        max = s1
        min = s2
    else:
        max = s2    
        min = s1
    if (len(max) - len(min)) != 1:
        return 2    
    max = list(max)
    min = list(min)
    for i in range(len(min)):
        if max[i] != min[i]:
            min.insert(i, max[i])
            if max == min:
                return 1
            else:
                return 2   
    min.append(max[i+1])   
    if max == min:
        return 1
    else:
        return 2 
def find_mismatch(s1,s2):
        s1 = s1.lower()
        s2 = s2.lower()
        count = 0
        if len(s1) != len(s2):
            return 2
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                count += 1            
        if count == 0:
            return 0
        elif count ==1 :
            return 1      
        else:
            return 2                   

def spelling_corrector(s1,s2):
    new_list = []
    s1=s1.split()     
    for old_char in s1:
        if len (old_char)<=2:
            new_list.append(old_char)
            continue
        flag = False
        for new_char in s2:
            result = find_mismatch(old_char,new_char)
            if result == 0:
                new_list.append(old_char)
                flag = True
                break
            elif result == 1:
                new_list.append(new_char)
                flag = True
                break
            else:
                result_2 = single_insert_or_delete(old_char, new_char)
                if result_2 == 1:
                    new_list.append(new_char)
                    flag = True
                    break
        if flag == False:            
            new_list.append(old_char)        
    sign = " "        
    new_str = sign.join(new_list) 
    new_str = new_str.lower()    
    return new_str


print(spelling_corrector('programing is fan and eesy', ['programming','this','fun','easy','book' ]))    