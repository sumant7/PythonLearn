#recusrion is a function that calls itself basically forming a kindof loop


#factorial function
#find the factorial of a number n

#loop method
#using n!=1*2*3*...*n
def factorial(n):
    ans=1
    for i in range(1,n+1):  
        ans=ans*i
    return(ans)  

print(factorial(10))    #prints 3628800



#recusrion method
# n! = 1 * 2 * 3 * 4...*n
# n! = [1 * 2 * 3 * 4... n-1] *n
# n! = n * (n-1)! = n * (n-1) * (n-2)! 

#be careful not to form infinite loop!
def factorial_r(n):
    if n==1 or n==0:     #just condition for when n becomes 1 or 0
        return 1   #prevents infinite loop
    return n*factorial_r(n-1)   #function calls itself

print(factorial_r(10))    #prints 3628800


