#string is a collection of characters
#single quote or souble quote can be used in a string
a= '''triple quote is used when "(double quote) or '(single quote) is a part of string
or a newline is needed'''


name= "Sumant Chaudhary"
greeting = "Good morning!, "

#concatination of string
concat = greeting + name   
print(concat)   #output is Good morning!, Sumant Chaudhary


#indexing
#indexing starts from 0
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# S u m a n t   C h a u  d  h  a  r  y
print(name[4])   #output is n
# name[4]= "s"  this will not work




#negative indexing
# useful when you don't know the length and want to print last character
# last character of a string is indexed as -1
#-16 -15 -14 -13 -12 -11 -10-9 -8 -7 -6 -5 -4 -3 -2 -1
# S   u   m   a   n   t      C  h  a  u  d  h  a  r  y
#|neg index| + positive index = length




#string slicing
print(name[0:3])  #output is Sum      from index 0 to 2
print(name[4:8])  #output is nt C     from index 4 to 7
print(name[:3])   #blank is treated as 0, output is Sum
print(name[5:])   #here blank is last index, output is t Chaudhary




#slicing with skipping  [start: end : skip value]
print(name[1:4:1])   #output is same as name[1:4]
#skips 0 characters after printing 1 character

print(name[0:5:2])   #output is Smn  NOT Suman
#it skipped 1 character after printing 1 character each time 

print(name[0::3]) #output is Sa ahy
#it skipped 2 characters after printing 1 character each time










#fstrings
num=5
i=2
print(f"{num}X{i}={num*i}")
#outputs 5X2=10
