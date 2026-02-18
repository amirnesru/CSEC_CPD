Petra = list(map(int,input().split())) 
Garaar = list(map(int,input().split()))
a=0
for i in range(2):
    if Petra[i]!=Garaar[i]:
        a+=1
print(a)        
