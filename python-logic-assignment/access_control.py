age = int(input("Enter your age: "))
id_input = input("Do you have an ID card (True/False): ").strip().lower()

has_id = id_input == "true"

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
