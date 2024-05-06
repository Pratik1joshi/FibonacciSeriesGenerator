import fibonacci

def main():
    print("Starting main...")

    number = int(input("Enter the length pf fibonacci series: "))

    series = fibonacci.get_fibonacci_series(number)
    
    print(series)

main()    