x=input("enter a sequence of brackets  ")
char1=0
char2=0
for i in x:
    if i=="(":
        char1+=1
    elif i==")":
        char2+=1
    if char2 > char1:
        break    
if char1==char2:
    print("TRUE")
else:
    print("FALSE")                
