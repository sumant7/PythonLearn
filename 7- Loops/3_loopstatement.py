#break statement is used to break a loop in the middle
for i in range(7):
    print(i)
    if(i==4):
        break          #when i becomes it exits the loop

# outputs
# 0
# 1
# 2
# 3
# 4


#for with ELSE only executes if loop is complete not when broken







#continue statement is used to SKIP one iteration of loop
for i in range(7):
    if(i==4):
        continue    #when i=4 it skips this iteration without printing
    print(i)    
#after continue is encountered any program inside loop below continue is skipped for one iteration
# outputs
# 0
# 1
# 2
# 3
# 5
# 6






#pass statement istructs to do nothing
if i>0:       
    pass         #do nothing

#if pass was not witten onle if i>0: was written then error would come 