# 123456=>A
# 456=>B output:yes
# 4523=>A 
# 1235=>B  output no 
a=int(input())
b=int(input())
t=len(str(b))
if a%(int(pow(10,t)))==b:
    print('yes')
else:
    print('no')
    
