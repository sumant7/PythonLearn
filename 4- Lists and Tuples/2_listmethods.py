a= [1,2,3,4,5,6,9,8]


#sort method sorts the original list not returning anything
b = a.sort()
print(a)   #outputs [1, 2, 3, 4, 5, 6, 8, 9]
print(b)   #outputs None
#hence simple write a.sort()



#reverse methods reverses
a.reverse()
print(a)   #outputs [9, 8, 6, 5, 4, 3, 2, 1]



#append methods appends at the end of the list
a.append(69)
print(a)   #outputs [9, 8, 6, 5, 4, 3, 2, 1, 69]



#insert functions inserts at given position   .insert(index, element )
a.insert(2,34)
print(a)  #outputs [9, 8, 34, 6, 5, 4, 3, 2, 1, 69]     34 is at index 2



#pop removes an index
a.pop(2)
print(a)   #outputs [9, 8, 6, 5, 4, 3, 2, 1, 69]     34 was index 2 so removed



#removes the given element
a.remove(69)
print(a)   #outputs [9, 8, 6, 5, 4, 3, 2, 1]    69 was removed sadly


#count returns the count of an element in the list
print(a.count(69))   #outputs 0