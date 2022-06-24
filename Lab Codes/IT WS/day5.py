#Change the Kth element of dictionary to 'String'
a={1:"Apple",2:"Banana",3:"Pear",4:"Fruit"}
x=0
print(a)
k=int(input())
a[k]="String"
print(a)    
print("----------------")

#Group the similar elements of a list into a dictionary
lol=[420,420,420,420,21,12,21,21,33,66,66,66,69,777,777,777,777]
print(lol)
grp={}
for x in lol:
    grp[x]=0
for x in lol:
    grp[x]+=1    
print(grp)    
print("----------------")

#Convert Matrix To Dictionary
t = [[4, 5, 6], [1, 3, 5], [3, 8, 1], [10, 3, 5]]
print(t)
d={i:j for i,j in enumerate(t,1)}
print(d)
print("---------------")

#Convert Tuple List To Dicionary
tuples = [('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]
result = dict(tuples)
print(result)
print("----------------")

#Sort the elements of the dictionary
d={9:'i',3:'c',13:'m',24:'x',1:'a'}
print(d)
ans=dict(sorted(d.items(),key=lambda x:x[1]))
print(ans)
print("------------------")