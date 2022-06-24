#1
x=input("Enter a string \n")
l=len(x)
if(l<2):
    print(" Insufficient Length \n")
else:
    z=x[0:2]+x[-2:] 
    print(z," ")  

#2
x=input("Enter A String \n")
lel=x[0]
lol=x[1:]
ans=lol.replace(lel,'$')
ans=lel+ans
print(ans)   

#3
x=input("Enter A string \n")
l=len(x)
if(l>=3):
    c=x[-3:]
    if(c=='ing'):
        ans=x+'ly'
    else:
        ans=x+'ing'
else:
    ans=x
print(ans)       

#4
x=input("Enter A String \n")
z=x.find("not")
y=x.find("poor")
if(z>0 and y>0 and z<y):
    ans=x.replace(x[z:y+4],'good')

if(ans==''):
    ans='Peasant'
print(ans)

#5
lol=["Archit","Sahay","lmao","lol","sed","ded","Depression"]
mx=-1
for x in lol:
    if(len(x)>mx):
        mx=len(x)
        mxs=x
print("Longest Word: ",mxs," ",mx)        

#6
x=input("Enter A Sentence \n")
lol=set(x.split())
for lel in lol:
    z=x.count(lel)
    print(lel," : ",z )
    
#7
def inser(loc,lol,ins):
    ans=lol[0:loc+1]+ins+lol[loc+1:]
    return ans
x=input("Enter A String \n") 
l=int(input("Enter Index to insert at \n"))
z=input("Enter A String to insert \n")
lol=inser(l,x,z)
print(lol)   

#8
def fir3(x):
    l=len(x)
    if(l>=3):
        ans=x[0:3]
    else:
        ans=x
    return ans
x=input("Enter A string \n")
lol=fir3(x)
print(lol)   

#9
for i in range(0,6):
    for j in range(0,i):
        print('* ',end='')
    print()    
for i in range(4,0,-1):
    for j in range(0,i):
        print('* ',end='')
    print()

#10
print(0)
for i in range(1,7):
    if(not(i%3==0)):
        print(i)

#11
for lol in range(1,50):
    if(lol%3==0 and not(lol%5==0)):
        print('Fizz')
    if(not(lol%3==0) and lol%5==0):
        print('Buzz')  
    if(lol%3==0 and lol%5==0):
        print('FizzBuzz')       

#12
n=int(input("Enter no. of elements \n"))
lol=[]
for i in range(0,n):
    z=input()
    lol.append(z)
print(lol)    
for ded in lol:
    if(ded =='0101' or ded =='1010' or ded =='1111'):
        print(ded,' ',end='')
