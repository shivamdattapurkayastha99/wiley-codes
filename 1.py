# wap to find middle element in the array 
a=int(input('Enter the length'))
if a%2==0:
    print("Your length is even program exits")
    exit(0)
    
print("Enter the elements of the array")
b=[int(input())for i in range(a)]
print("Middle element of the array is ")
print(b[a//2])


