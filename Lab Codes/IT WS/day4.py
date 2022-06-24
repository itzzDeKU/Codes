#Create Tuple from list by storing reverse of elements
A,B = [34,56,78], []
for i in A :
    x = str(i)
    x = x[::-1]
    B.append(x)
t = tuple(B)
print(t)

#Sort Tuple
lol=(12,420,69,7,666,777,2001,28,619)
x=sorted(lol)
ans=tuple(x)
print(ans)

#Merge Tuple
a=('a','b','c')
b=(1,2,3)
c=a+b
print(c)

#Divisible by n
lol=[1,3,2,4,5,6,7,11,9,10,8,12]
ans=[]
k=int(input("K: "))
for x in lol:
    if x%k==0:
        ans.append(x)
anst=tuple(ans)
print(anst)        

#Tuple Matrix to Tuple List
t = [[(4, 5), (7, 8)], [(10, 13), (18, 17)], [(0, 4), (10, 1)]]
print("The original list is : " + str(t))
temp = [e for s in t for e in s]
res = list(zip(*temp))
print("The converted tuple list : " + str(res))
