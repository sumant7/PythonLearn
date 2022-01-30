#a list is a collection of any data type
#indexing is from 0 like strings and -ve indexs also works same
a= [1,2,3,4,5,6,9,8]  #a list
a[0]= 69   #this will work unlike strings
print(a)   #output [69, 2, 3, 4, 5, 6, 9, 8]




#we can create list of different data types
b=[1,23.5,"hello",True]   #this is valid


#slicing similar to list
print(a[1:4]) #output [2, 3, 4]
print(a[1:9:2]) #output [2, 4, 6, 8]