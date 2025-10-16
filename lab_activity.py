# Task 1: Basic Calculator 
def task1_basic_calculator():
    print("\nTask 1: Basic Calculator\n")
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print(f"\na = {a}, b = {b}")
    print(f"Addition: {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Multiplication: {a * b}")
    print(f"Floating-Point Division: {a / b}")
    print(f"Integer Division: {a // b}")
    print(f"Modulus: {a % b}")
    print(f"Exponentiation: {a ** b}")

# Task 2: Order of Operations Challenge
def task2_order_of_operations():
    print("\nTask 2: The Order of Operations Challenge\n")
    result1 = 5 + 3 * 2 ** 2
    result2 = (5 + 3) * 2 ** 2
    result3 = 10 % 3 + 5 * 2
#Output:
    #result 1 = 17
    #result 2 = 32
    #result 3 = 11
    
    print("Order of Operations Results:")
    print(f"1. 5 + 3 * 2 ** 2 = {result1}")
    print(f"2. (5 + 3) * 2 ** 2 = {result2}")
    print(f"3. 10 % 3 + 5 * 2 = {result3}")

# Task 3: Unit Conversion Challenge
def task3_unit_conversion():
    print("\nTask 3: Unit Conversion Challenge\n")
    inches = int(input("Enter the number of inches: "))

    feet = inches // 12
    remaining_inches = inches % 12

    print(f"{inches} inches is equal to {feet} feet and {remaining_inches} inches.")

# Task 4: Movie Ticket Price Decider 
def task4_movie_ticket_price():
    print("\nTask 4: Movie Ticket Price Decider\n")
    base_price = 12

    age = int(input("Enter your age: "))
    is_student = input("Are you a student? (True/False): ").lower() == "true"

    if age <= 12:
        final_price = base_price - 3
    elif age >= 65:
        final_price = base_price - 4
    elif is_student:
        final_price = base_price - 2
    else:
        final_price = base_price

    print(f"\nAge: {age}")
    print(f"Is student? {is_student}")
    print(f"Your ticket price is ${final_price}.")

# Task 5: Secure System Login Simulator
def task5_secure_login():
    print("\nTask 5: Secure System Login Simulator\n")

    username = "janrony"
    password = "tagaltal"
    correct_2fa_code = "242507"

    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    two_fa_input = input("Is 2FA enabled? (y/n): ").lower()

    is_2fa_enabled = (two_fa_input == "y")

    if is_2fa_enabled:
        input_2fa = input("Enter 2FA code: ")
    else:
        input_2fa = ""

    if (
        input_username == username
        and input_password == password
        and (not is_2fa_enabled or input_2fa == correct_2fa_code)
    ):
        print("Login successful!")
    else:
        print("Login failed!")

#Bonus Challenge
def bonus_shipping_calculator():
    print("\nBonus: Shipping Cost Calculator\n")
    base_cost = 10

    weight = float(input("Enter total weight of the order (in pounds): "))
    destination = input("Enter shipping destination (domestic/international): ").lower()
    membership = input("Enter membership type (standard/premium): ").lower()

    total_cost = base_cost

    if weight > 20:
        total_cost += 5

    if destination == "international" and membership != "premium":
        total_cost *= 2

    if membership == "premium":
        total_cost *= 0.8

    print(f"\nShipping Summary:")
    print(f"Weight: {weight} lbs")
    print(f"Destination: {destination.capitalize()}")
    print(f"Membership: {membership.capitalize()}")
    print(f"Total shipping cost: ${total_cost:.2f}")

# MAIN MENU
def main():
    print("\n=== MENU ===")
    print("Task 1: Basic Calculator")
    print("Task 2: Order of Operations")
    print("Task 3: Unit Conversion")
    print("Task 4: Movie Ticket Price")
    print("Task 5: Secure System Login")
    print("Bonus: Shipping Cost Calculator")
    print("\nType 'Exit' to end the program.")

    while True:
        choice = input("\nEnter your choice (Task 1/Task 2/.../Bonus/Exit): ").strip().lower()

        if choice == "task 1":
            task1_basic_calculator()
        elif choice == "task 2":
            task2_order_of_operations()
        elif choice == "task 3":
            task3_unit_conversion()
        elif choice == "task 4":
            task4_movie_ticket_price()
        elif choice == "task 5":
            task5_secure_login()
        elif choice == "bonus":
            bonus_shipping_calculator()
        elif choice == "exit":
            print("\nExiting... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
