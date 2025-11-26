# ----------------------------- 
# Welcome Section 
# ----------------------------- 
print("\n" + "="*60) 
print("🎓 Welcome to Student Profile Generator CLI") 
print("="*60) 
print("This tool will collect your details and generate your profile card.") 
print("You will also learn Python basics like:\n- Variables\n- Data Types\n- Operators\n- String Functions\n- File Handling\n") 
# ----------------------------- 
# Task 2: Input & Variables 
# ----------------------------- 
full_name = input("Enter your full name: ") 
roll_no = input("Enter your roll number: ") 
program = input("Enter your program (e.g., BCA): ") 
university = input("Enter your university name: ") 
city = input("Enter your city: ") 
age = int(input("Enter your age: "))  # type conversion 
hobby = input("Enter your hobby: ") 
print("\n✅ Student Data Recorded Successfully!\n") 
# ----------------------------- 
# Task 3: Operators Demonstration 
# ----------------------------- 
print("="*60) 
print("🔢 Python Operators Demonstration") 
print("="*60) 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: ")) 
# Arithmetic 
print("\n-- Arithmetic Operations --") 
print(f"{num1} + {num2} = {num1 + num2}") 
print(f"{num1} - {num2} = {num1 - num2}") 
print(f"{num1} * {num2} = {num1 * num2}") 
print(f"{num1} / {num2} = {num1 / num2}") 
print(f"{num1} % {num2} = {num1 % num2}") 
print(f"{num1} ** {num2} = {num1 ** num2}") 
print(f"{num1} // {num2} = {num1 // num2}") 
# Assignment Operators 
a = num1 
a += 5 
print("\n-- Assignment Operator Example --") 
print(f"num1 += 5 → {a}") 
# Comparison 
print("\n-- Comparison Operators --") 
print(f"{num1} > {num2} : {num1 > num2}") 
print(f"{num1} == {num2} : {num1 == num2}") 
# Logical 
print("\n-- Logical Operators --") 
print(f"({num1} > {num2}) and ({num1} != {num2}) : {(num1 > num2) and (num1 != 
num2)}") 
# Identity 
print("\n-- Identity Operators --") 
print(f"num1 is num2 : {num1 is num2}") 
# Membership 
print("\n-- Membership Operators --") 
sample_string = full_name.lower() 
print(f"'a' in your name? : {'a' in sample_string}") 
# ----------------------------- 
# Task 4: String Operations 
# ----------------------------- 
print("\n" + "="*60) 
print("🔤 String Formatting & Methods Demo") 
print("="*60) 
print("Uppercase name:", full_name.upper()) 
print("Lowercase name:", full_name.lower()) 
print("Title case name:", full_name.title()) 
print("Name length:", len(full_name)) 
print("Replace a with @:", full_name.replace("a", "@")) 
# ----------------------------- 
# Task 5: Profile Card Output 
# ----------------------------- 
print("\n" + "-"*60) 
print(" STUDENT PROFILE SYSTEM") 
print("-"*60) 
print(f"Name:            {full_name}") 
print(f"Roll No:         {roll_no}") 
print(f"Course:          {program}") 
print(f"University:      {university}") 
print(f"City:            {city}") 
print(f"Age:             {age}") 
print(f"Hobby:           {hobby}") 
print("-"*60) 
print("Welcome to Python Programming! ✅") 
print("-"*60) 
# ----------------------------- 
# Task 6: Save Profile (Bonus) 
# ----------------------------- 
save = input("\nDo you want to save your profile? (yes/no): ").lower()
if save == "yes":
    with open("student_profile.txt", "w") as file:
        file.write("STUDENT PROFILE\n")
        file.write("-" * 50 + "\n")
        file.write(f"Name: {full_name}\nRoll No: {roll_no}\nCourse: {program}\nUniversity: {university}\nCity: {city}\nAge: {age}\nHobby: {hobby}\n")
        file.write("-" * 50)
    print("\n✅ Profile saved to student_profile.txt")
else:
    print("\n✅ Profile not saved.")
    print("\n🎯 Thank you for using this program!")
