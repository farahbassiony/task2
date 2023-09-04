a=[]
n=int(input("Number of elements in list:\n"))
print("enter the numbers of the list")
for i in range(n):
   l=int(input())
   a.append(l)
x=int(input("enter the required number  "))
for i in range(n-1):
   y=x-int(a[i])
   if y in a:
      print("the two numbers are found which are "+str(y)+" and " +str(a[i])+" so their sum is "+str(x))
      break
   else:
      print("the 2 numbers are not found") 
      break  
      
