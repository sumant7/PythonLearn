#conditionals statements      

a=45
if(a>3):
    print("a is greater than 3")    #the 4 spaces on the left of print statment means that this statement in inside if
    print("This is If statement")

elif(a>7):
    print("a is greater than 7")

elif(a>16):
    print("a is greater than 19")

elif(a>69):
    print("a is greater than 69")

else:
    print("a is ")


#output is 
#a is greater than 3
#Hue Hue

#first if condition is checked
#elif is only excuted when if does not excute
#else is only excuted when all elif conditions fail to excute


#if statements can be used indepently but not else and elif

#multi if statement


b=69
if(b>3):
    print("b is greater than 3")
if(b>7):
    print("b is greater than 7")
if(b>16):
    print("b is greater than 19")
if(b>69):
    print("b is greater than 69")
else:                #this else is only dependent on the last if
    print("Else")

#output is
# b is greater than 3
# b is greater than 7
# b is greater than 19
# Else

#if is excuted independently of other ifs


