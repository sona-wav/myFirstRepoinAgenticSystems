name = input("Enter your name: ")
age = int(input("Enter your age: "))

active_input = input("Are you an active user (True/False): ").strip().lower()

is_active = active_input == "true"

print(f"User {name} is {age} years old. Active status: {is_active}")
