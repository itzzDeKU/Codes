#Find Odd no.s in the List
lol=[1,2,3,4,5,6,7]
lmao=[]
for i in lol:
    if i%2==1:
        lmao.append(i)
print(lmao)        

#Merge 2 lists
lol=[1,2,3,4]
lmao=[9,8,7,6,5]
ans=[]
for i in lol:
    ans.append(i)
for i in lmao:
    ans.append(i)    
print(ans)

#Rotate List with Middle Point is fixed
lol=[1,2,3,4,5,6,7,8,9,10]
l=len(lol)
print(l//2)
ans=lol[l//2:]
ans=ans+lol[0:l//2][::-1]
print(ans)

#Sort the List in Ascending Order
k=[9,3,6,7,2,0,1]
l=len(k)
for i in range(0,l):
    for j in range(i+1,l):
        if k[i]>k[j]:
            c=k[i]
            k[i]=k[j]
            k[j]=c
print(k)   

#Remove k consecutive elements
lol=[1,2,3,4,5,6,7,8,9]
l=len(lol)
k=int(input(f"Enter no. removals(<={l})\n"))
print(lol[0:l-k])   

#Find the Kth String in list
lol=["int","float","ost","final","Archit","Sahay"]
l=len(lol)
k=int(input(f"Enter string pos to find(<={l}) \n"))
print(lol[k-1])

#Freq of elements
lmao=[1,2,2,2,3,3,420,420,69,420,69]
ans=[]
for i in lmao:
    if i not in ans:
        ans.append(i)
        print(f"Freq. of {i} : "+str(lmao.count(i)))

#Remove repeated elements
lmao=[1,2,2,2,3,3,420,420,69,420,69]
print(*set(lmao))
