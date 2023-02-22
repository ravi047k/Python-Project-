# define function to perform addition operation
def add(x, y):
    return x + y

# define function to perform subtraction operation
def subtract(x, y):
    return x - y

# define function to perform multiplication operation
def multiply(x, y):
    return x * y

# define function to perform division operation
def divide(x, y):
    return x / y

# display options to user
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# ask user to input choice of operation
choice = input("Enter choice (1/2/3/4): ")

# ask user to input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# perform operation based on user's choice
if choice == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1,num2))

else:
    print("Invalid input")

