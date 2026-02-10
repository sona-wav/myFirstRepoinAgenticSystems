balance = int(input("Enter account balance: "))
withdrawal = int(input("Enter withdrawal amount: "))
verified_input = input("Are you verified (True/False): ").strip().lower()

is_verified = verified_input == "true"

if is_verified and withdrawal <= balance:
    print("Withdrawal successful")
else:
    print("Transaction denied")
