k,s=map(int , input().split())
a=0
while s>=k:
    s=s-k
    a+=1
a+=s    
print(a)
