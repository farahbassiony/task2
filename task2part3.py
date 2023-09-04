def anagram(x,y):
    if sorted(x)==sorted(y):
        return True
    return False
x=input("enter the first word ")
y=input("enter the second word  ") 
if anagram(x,y):
    print("The two words are anagrams")
else: 
    print("the two words are not anagrams")    
  
