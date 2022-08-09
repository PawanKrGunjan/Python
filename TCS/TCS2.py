n1=int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

#Create a list from n1 to n2
l=[]
for i in range(n1,n2):
    l.append(i)
#print(l)

#Canvert the type of each element of the list to string
L=[]
for j in l:
    L.append(str(j))

#L = [str(x) for x in l]
#L = list(map(str, l))
#print(L)

# Remove the element having same digits like 11, 22, 33....
s= set()
for x in L:
    i=0
    for i in range(len(x)):
        if x[i] == x[0]:
           pass
        else:
            s.add(x)
       
       
#ReConvert the each element of output 
print(s)
Output = set(map(int, s))
print(list(Output))

