a="Hello"   #string
b= 69#  an integer
c= 34.34  #decimal or floating point number.
d= '''triple quote is used when "(double quote) or '(single quote) is a part of string
or a newline is needed'''
e= True   #boolean
f= None   #we will see the use later. It literally represents nothing.

#keywords are predefined reserved words that perform a function.
#we can't use keywords as variables



#type of variable
print(type(a))  #output -<class 'str'> since string
print(type(b))  #output -<class 'int'> 
print(type(c))  #output -<class 'float'> 
print(type(d))  #output -<class 'str'> 
print(type(e))  #output -<class 'bool'> 
print(type(f))  #output -<class 'NoneType'> 



#variable naming
#naming a case sensitive
# 1a= 54 is invalid 
#variable name can only start with alphabet and _ but can contain numbers after that
#no spaces allowed


#.format function
print("{greet} there!".format(greet=a))   #outputs Hello there!