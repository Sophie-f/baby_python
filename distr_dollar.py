import random as rn
a=[]
for i in range(0,100):  
    a.append(100)
print (a)    
def dis(persons):
    for person_1 in range(0,100): 
        if persons[person_1]>0:
            person_2=rn.randint(0,99) 
            while persons[person_2]==0:
                person_2=rn.randint(0,99)
            persons[person_1]=persons[person_1]-1
            persons[person_2]=persons[person_2]+1
for i in range (0,10000):
    dis(a)  
print (a)                      
