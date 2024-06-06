# Student Result Computing System

# Function to add a student's result
def add_result():
    name = input("Enter student's name: ")
    matricno = input("Enter matric number: ")
    ccode = input("Enter Course Code: ")
    marks = float(input("Enter marks: "))

    with open("results.txt", "a") as file:
        file.write(f"{name},{matricno},{ccode},{marks}\n")

# Function to display all results
def display_results():
    with open("results.txt", "r") as file:
        for line in file:
            name, matricno, ccode, marks = line.strip().split(",")
            print(f"Name: {name}, Matric No: {matricno}, Course Code: {ccode}, Marks: {marks}")

# Function to search a student's result
def search_result():
    matricno = input("Enter matric number to search: ")

    with open("results.txt", "r") as file:
        for line in file:
            name, matric_search, ccode, marks = line.strip().split(",")
            if matric_search == matricno:
                print(f"Name: {name}, Matric No: {matricno}, Course Code: {ccode}, Marks: {marks}")
                break
        else:
            print("No result found.")

# Main menu
while True:
    print("1. Add Result")
    print("2. Display All Results")
    print("3. Search Result")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_result()
        print()
    elif choice == "2":
        display_results()
        print()
    elif choice == "3":
        search_result()
        print()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
