arr=[600,800,45,341,10000]
max=arr[0]
min=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]>max:
        max=arr[i]
print(max)
for i in range(1,n):
    if arr[i]<min:
        min=arr[i]
print(min)

    
    