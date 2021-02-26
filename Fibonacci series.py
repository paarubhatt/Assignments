#Recursive function to display fibonacci series upto 8 terms
def Fibonacci(n):
    #To check given term is negative number
     if n < 0:
         print("Invalid Input")
     #To check given term is 0  ,returns 0
     elif n == 0:
         return 0
     # To check given term is either 1 or 2 because series for 1 or 2 terms will be 0 1
     elif n == 1 or n == 2:
         return 1
     #Return a series until term value exceeds
     else:
         return Fibonacci(n-1)+Fibonacci(n-2)
#initialized term value
term = 8
#For loop prints the fibonacci series upto 8 terms
for i in range(term):
    print(Fibonacci(i))