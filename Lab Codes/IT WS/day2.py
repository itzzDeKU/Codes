#Add 2 Strings
str  ='Aman'
print(str[0:]*2+"TEST")

#Fulll Name
str1=input("Enter First Name \n")
str2=input("Enter Middle Name \n")
str3=input("Enter Last Name \n")
str4=str1+' '+str2+' '+str3
str5=str1[0]+'.'+str2[0]+'.'+str3[0]+'.'
print(str4)
print(str5)

#Function Length and String comparisons
str1=input("Enter a word \n")
str2=input("Enter another one \n")
l1=len(str1)
l2=len(str2)
z1=0
for i in str1:
   z1=z1+ord(i) 
z2=0
for i in str2:
   z2=z2+ord(i) 
m=max(l1,l2)
if(m==l1 and m!=l2):
 print(str1)
elif m!=l1 and m==l2:
 print(str2)
elif(m==l1 and m==l2):
    if(z1>z2):
     print(str1) 
    elif(z2>z1):
     print(str2)   
    else:
     print(str1+' '+str2)   
  
#To check if a string is Palindrome or not
n="LOLO"
r=""
for i in n:
    r=i+r    
if (r==n):
    print("Palindrome \n")
else:
    print("Not Palindrome \n")       

#To reverse a string
x=input()
r=""
for i in x:
    r=i+r
print(r)

#To copy one string in another
a="LOL"
b="LMAO"
print(b)
b=''
for i in a:
  b=b+i
print(b)

#Swap two strings
a="LOL"
b="LMAO"
print(a+' '+b)   
c=b
b=''
for i in a:
  b=b+i
a=''
a=c 
print(a+' '+b)    