def fibonacci(n):
    if n == 0:
       return n
    elif n == 1:
        return n  
    else:
       return(fibonacci(n-1) + fibonacci(n-2))
################################################################
def lucas(num) :
    a = 2
    b = 1
    if (num == 0) :
        return a
    # generating number
    for i in range(2, num + 1) :
        c = a + b
        a = b
        b = c
    return b
######################################################################
def sum_series(num, num1, num2):
    if type(num) != int:
        return ("Invalid Input")
    elif num < 0:
        return ("Invalid Negative Value")
    elif num == 0:
       return num1
    elif num == 1:
       return num2
    else:
       return (sum_series(num-1, num1, num2) + sum_series(num-2, num1, num2))