def binary_search(a,x,start,end):
     middle=0
     if start>end:
         return False
     else:
          middle = (end + start) // 2 
          if a[middle]==x:
              return True
          elif int(a[middle]) <int(x) :
            return binary_search(a, x, middle + 1, end)
          else:
            return binary_search(a, x, start, middle - 1)
               

a=[]
n=int(input("Number of elements in array:"))
for i in (0,n):
   l=int(input())
   a.append(l)
x=int(input("enter the element you are looking for  "))   
bin=binary_search(a,x,0,len(a)-1)
if(bin==True):
    print("the required item is found")
else:
    print("the item is  not in the list")    