N=int(input())

n=input().split()
v=input()
count=0
for i in n:
    if i==v:
        count+=1


print(count)
