#is and in

#is
a= None  
if(a is None):    #this condition is true because a points towards none
    print("Yes!")
else:
    print("No")
#outputs Yes!

#in
b=[1,2,56,69]
print(69 in b)   #outputs true
print(34 in b)   #outputs false

#in strings
s= "Hello There! Are you having a bad day?"
if 'bad' in s:
    print('Bad day')    #outputs Bad day