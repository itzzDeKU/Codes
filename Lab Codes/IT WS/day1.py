# #Area of Triangle
b=int(input("Breadth: "))
h=int(input("Height: "))
area=(b*h)/2
print("Area of Triangle: "+str(area))

# #Area of Triangle using Heron's formula
a=int(input("First Side: "))
b=int(input("Second Side: "))
c=int(input("Third Side: "))
s=(a+b+c)/2
harea=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of Triangle using Heron's Formula: "+str(harea))

# #Find S.I.
p=int(input("Principal Amount: "))
r=float(input("Annual Rate of Interest: "))
t=int(input("Time in Years: "))
si=(p*r*t)/100
print("Simple Interest: "+str(si))
print(f"Amount after {t} years: "+str(p+si))

#Find C.I.
cp=int(input("Principal Amount: "))
cr=float(input("Annual Rate of Interest: "))
ct=int(input("Time in Years: "))
amount=cp*((1+cr/100)**ct)
ci=amount-cp
print("Compound Interest: {0:.2f}".format(ci))
print("Amount after {0:d} years: {1:.2f}".format(ct,amount))

#Check Whether Given no. is float or integer
x=input("Enter a No. : ")
if('.'in x):
    print("Float")
else:
    print("Integer")    
