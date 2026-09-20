def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = float(input("Enter student marks: "))

    with open("student.txt", "a") as file:
        writer = file.write(f"{name},{age},{marks}\n")

def view_student():
    with open("student.txt", "r") as file:
        for i, line in enumerate(file, start=1):
            data = line.strip().split(",")

            print(f"Student {i}")
            print(f"Name: {data[0]}")
            print(f"Age: {data[1]}")
            print(f"Marks: {data[2]}")
            print("-"*20)

def search_student():
    search_name = input("Enter a student name: ")
    found = False

    with open("student.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0].lower() == search_name.lower():
                print("Student Found!")
                print(f"Name: {data[0]}")
                print(f"Age: {data[1]}")
                print(f"Marks: {data[2]}")
                print("")
                found = True

        if not found:
            print(f"Student {search_name} not found!")

def delete_student():
    delete_name = input("Enter student name: ")
    found = False

    with open("student.txt", "r") as file:
        lines = file.readlines()

    with open("student.txt", "w") as file:
        for line in lines:
            data = line.strip().split(",")

            if data[0].lower() == delete_name.lower():
                found = True
            else:
                file.write(line)

        if not found:
            print("Student not found.")
        else:
            print("Student delete successfully.")

def update_student():
    update_name = input("Enter student name: ")

    found = False

    with open("student.txt", "r") as file:
        lines = file.readlines()

    with open("student.txt", "w") as file:
        for line in lines:
            data = line.strip().split(",")


            if data[0].lower() == update_name.lower():
                new_name = input("Enter new name: ")
                new_age = int(input("Enter new age: "))
                new_marks = float(input("Enter new marks: "))

                data[0] = new_name
                data[1] = str(new_age)
                data[2] = str(new_marks)

                line = ",".join(data) + "\n"
                found = True
            file.write(line)

        if not found:
            print("Student not found!")
        else:
            print("Student data updated successfully")

while True:
    print("="*20)
    print("1. Add student\n2. View students\n3. Search student\n4. Update student\n5. Delete student")
    print("="*20)

    choice = input("Enter your choice: ")
    print("-"*20)

    if choice == "1":
        add_student()
    elif choice == "2":
        view_student()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    else:
        print("Please make a valid choice.")