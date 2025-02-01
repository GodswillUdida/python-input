# print()
# print("Hello woorld")

# name = input("Enter your name: ")
# print(f"Hello, {name}!  Welcome to Python.")

# user_name = "Godswill"
# age = 90
# height = 6.1
# is_student = True



def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

name = input("Enter your name: ")
age = get_integer ("Enter your age: ")
height = get_float("Enter your height in meters: ")
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"

# print("/n--- User Information ---")
print(f"Name       : {name}")
print(f"Age        : {age} years")
print(f"Height     : {height:.2f} meters")
print(f"Student?   : {'Yes' if is_student else 'No'}")
print(f"Hey {name}, you will turn 100 years old in {100 - age} years!")


# G
