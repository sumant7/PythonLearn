# relational and logical operators are also used with ifs

c= 69
if(c==69):     #relational operator
    print("Nice")
#output is Nice

if(c>50 and c<60):  #logical operator     
    print("Old!")   
#outputs nothing as 69 is >50 but is NOT <60

if(c>50 or c<60):   #logical operator
    print("Old!")   
#output is Old!