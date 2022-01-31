#function is basically a piece of code which you write once but use many times

marks=[86,93,98,96]
percentage= (sum(marks)/400)*100    #sum is a built in function 
print(percentage)   #outputs 93.25

#here sum is a function that we use just by calling sum()




#creating a user-defined function

def percent(marks):    #we defined a function which takes a list and returns percentage
    return  (sum(marks)/400)*100   #this part is function defintion

m2=[96,98,99,98]

print(percent(m2))     #this is function call
#outputs 97.75





#default parameter value

def greet(name): #this function takes a string and prints, returns nothing
    print("Good Day,"+ name)

greet("Harry")   #outputs Good Day,Harry
greet()   #gives error as no parameter is provided




def greet2(name="Sumant"):     #we have set the default parameter as 'Sumant'
    print("Good Day,"+ name)

greet2("Stacy")   #outputs  Good Day,Stacy
greet2()    #outputs Good Day,Sumant