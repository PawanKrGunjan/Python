def fibonacci(n):
    
    #Write your code below to calculate
    #to calculate the nth fibonacci number
    fi = f_i = f__i = 1
    for i in range(3,n+1):
        fi = f_i + f__i
        f_i = f__i
        f__i= fi
    return fi

print(fibonacci(50))
print(fibonacci(100))
print(fibonacci(101))
print(fibonacci(103))