n=int(input())
arr=[]
for i in range (n):
    s=input()
    arr.append(s)
for x in arr[::2]:
    print(x)
