def addition(a, b):
    return a + b

def mul_numbers(a, b):
    return a * b

def subtract_numbers(a, b):
    return a - b

def divide_numbers(a, b):
    return a // b

def exponent(a, b):
    return a ** b

def main():
    while True:
        print("=== My Calculator ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponential")
        
        choice = input("What operation do you want to perform: ")

        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if choice == "1":
            print("Result:", addition(a, b))
        elif choice == "2":
            print("Result:", subtract_numbers(a, b))
        elif choice == "3":
            print("Result:", mul_numbers(a, b))
        elif choice == "4":
            print("Result:", divide_numbers(a, b))
        elif choice == "5":
            print("Result:", exponent(a, b))
        else:
            print("invalid input")

if __name__  == "__main__":
    main()




