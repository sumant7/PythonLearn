#for loop is used to iterate

l=["Hello","Hi","Hey"]
for item in l:    #item here is variable
    print(item)
#outputs
# Hello
# Hi
# Hey







#range Function using for loop
#range(5) is same as range(0,5)
for i in range(5,12):    #iterates starting from 5 to 11
    print(i)
#outputs
# 5
# 6
# 7
# 8
# 9
# 10
# 11


#full syntax range(start,stop,step-size)
for i in range(5,12,2):       #not used usually
    print(i)
#skipped every 2nd item
# outputs
# 5
# 7
# 9
# 11





for i in range(7):     
    print(i)
else:               #not used much
    print("This is else with for")

# outputs
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# This is else with for




#patterns using for loop
for i in range(4):
    print("*"*(i+1))   #prints * i+1 times

# *
# **
# ***
# ****