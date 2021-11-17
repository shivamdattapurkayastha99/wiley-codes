# if the input contain only numbers then output true else output false 
a=input()
if a.isalpha():
    print('false')

elif a.isdigit():
    print('true')
else:
    print('false')
