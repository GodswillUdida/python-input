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
            age  = int(input(prompt))
            if age >= 100:
                print("Wow! You have already turned 100 years old! But let's enter a valid age.")
                continue
            if age <= 0:
                print("❌ Age cannot be negative. Please enter a valid number.")
                continue
            return age
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
            
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")
 
def get_answer(prompt):
    while True:
        is_student = input(prompt).strip().lower() 
        if is_student in ["yes", "no"]:
          is_student = is_student == "yes"
        print("❌ Invalid input! Please type 'yes' or 'no'.")
             

name = input("Enter your name: ")
age = get_integer("Enter your age: ")
height = get_float("Enter your height in meters: ")
is_student = get_answer("Are you a student? (yes/no): ")



print()

print(" User Information ")
print(f"Name       : {name}")
print(f"Age        : {age} years")
print(f"Height     : {height:.2f} meters")
print(f"Student?   : {'Yes' if is_student else 'No'}")
print(f"Hey {name}, you will turn 100 years old in {100 - age} years!")


# G
