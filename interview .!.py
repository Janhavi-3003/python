#fibonacci series
def fibonacci(n):
    
   a,b=0,1
   for i in range (n):
       fibonacci.append(a)
       a,b=b,a+b
       return fibonacci
n=int(input())
print(f"enter the number of terms:")
print(f"fibonacci series with {n} terms :{fibonacci(n)}")
        
