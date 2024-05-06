#Fibonacci series 0, 1, 1, 2, 3, 5, 8, 13,........

def get_fibonacci_series(num):

    if not isinstance(num, int):
        print("Invalid input, must be positive integer")

    if num <= 0:
        print("Invalid Input, Input must be greater than 0")
        return None
    
    fibonacci_series = [0,1]

    for i in range(num-2):
        next_item = fibonacci_series[-1]+fibonacci_series[-2]
        fibonacci_series.append(next_item)

    return fibonacci_series    