# count total uppercase and lowercase characters in an input string 
s=input()
u=0
l=0

for i in s:
    if i!=' ' and i.isupper():
        u+=1
    elif i!=' ' and i.islower():
        l+=1
print(s)
print('Uppercase characters :',str(u))
print('Lowercase characters :',str(l))

