#while loops runs until the given conditions remains true
from asyncore import loop


i=0
while i<10:   #condition
    print("Yes",i)
    i+=1    #each time loop runs i increases by one
#when i becomes 10 the condition becomes false hence loop is exited
#yes is printed 10 times


#print numbers from 1 to 50
# x=1
# while x<=50:
#     print(i)
#     i=i+1






#print all list elements using while loop
l=[11,21,31,41,51]
x=0
while  x<len(l):
    print(l[x])
    x=x+1
#outputs
# 11
# 21
# 31
# 41
# 51