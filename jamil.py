# Fibonnaci Sequence = 0,1,1,2,3,5,8....
n = int(input("How many Fibonacci numbers do you want? "))

fib = []

a = 0
b = 1

for i in range(n):
    fib.append(a)
    c = a + b
    a = b 
    b = c 

print(fib)
