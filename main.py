arr = []
for i in range(int(input())):
    arr.append(int(input()))
# candy left to right, candy right to left, and candy array
candy_lr = [1]*(len(arr))
candy_rl = [1]*(len(arr))
candy = []

# traverses from left to right and assigns candy to students
for i in range(1,len(arr)):
    if arr[i]>arr[i-1]:
        candy_lr[i] = candy_lr[i-1]+1

# traverses from right to left and assigns candy to students
for i in range(len(arr)-2,-1,-1):
    if arr[i]>arr[i+1]:
        candy_rl[i] = candy_rl[i+1]+1

#calculates the total candy needed
for i in range(0,len(arr)):
    candy.append(max(candy_lr[i],candy_rl[i]))
print(sum(candy))