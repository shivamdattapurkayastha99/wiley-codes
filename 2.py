# sort an array 
print("Enter the length of the array")
a=int(input())
b=[]
for i in range(a):
    b.append(int(input()))
b.sort(reverse=True)
print(b)


