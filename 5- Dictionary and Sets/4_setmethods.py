a = set()


#add method    adds to end
a.add((1,2,3))   #tuple inside set is valid since it's hashable
a.add(4)
a.add(5)
a.add(5)    #remember this has not effect since set is a non repetitive collection
a.add(5.0)   #won't make a difference either
#a.add([1,2,3]) will give error
#we can't add dictionary or list inside set since they both are unhashable(can change)
print(a)   #output {(1, 2, 3), 4, 5}



#len returns length
print(len(a))   #ouputs 3  since (1,2,3) is one item


#remove
a.remove(5)   #removes 5
print(a)     #outputs {(1, 2, 3), 4} 



#pop   removes random value    it is used to choose a random value
print(a.pop())    #ouput (1, 2, 3)   #this has been removed
print(a)     #output {4}



#clear 
a.clear()   #empties set


#just adding back elements
a.add(1)
a.add(2)
a.add(3)
a.add(4)
a.add(5)


b=set()
b.add(1)
b.add(2)
b.add(3)
b.add(8)
b.add(9)


#union  returns union of 2 sets
u= a.union(b)
print(u)    #outputs {1, 2, 3, 4, 5, 8, 9}



#intersetion  returns intersection of 2 sets
i = a.intersection({1,2,3,7,8,9})
print(i)   #outputs {1, 2, 3}