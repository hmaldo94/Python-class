def main():
    # Step 1: Create an empty dictionary variable to store student information
    student_info = {}

    # Step 2: Create a new key using the student's name as a key in the student information dictionary
    # Step 3: Each student should have an ID, GPA, credits completed, and a list of grades
    student_info["Alice"] = {"ID": "001", "GPA": 3.7, "Credits Completed": 45, "Grades": [90, 85, 88]}
    student_info["Bob"] = {"ID": "002", "GPA": 3.5, "Credits Completed": 50, "Grades": [80, 75, 78]}
    student_info["Charlie"] = {"ID": "003", "GPA": 3.9, "Credits Completed": 60, "Grades": [95, 90, 92]}

    # Step 4: Print the dictionary containing all student information
    print("Full Student Information Dictionary:")
    print(student_info)

    # Step 5: Print a heading announcing listing the student names
    print("\nStudent Names:")

    # Step 6: Use a loop to print each student's name in the dictionary
    for student in student_info.keys():
        print(student)

    # Step 7: Print a heading announcing the accessing of student information <<<<<<<------------------
    print("\nAccessing Student Information:")

    # Step 8: Print a second heading with the fields Name, ID, GPA, Credits Completed, & Grades
    print("\nName\tID\tGPA\tCredits Completed\tGrades")

    # Step 9: Use a loop to print each student's name, ID, GPA, credits completed, and grades
    # Step 10: Use the items method for dictionaries to access both key/value pair items
    for name, info in student_info.items():
        print(f"{name}\t{info['ID']}\t{info['GPA']}\t{info['Credits Completed']}\t\t{info['Grades']}")

    # Step 11: Print a heading announcing removing a student
    print("\nRemoving Student (Bob):")

    # Step 12: Use the pop method to remove the student from the dictionary
    student_info.pop("Bob")

    # Step 13: Print the updated student information dictionary
    print("\nUpdated Student Information Dictionary:")
    print(student_info)

    # Step 14: Print a heading announcing the accessing of GPA information
    print("\nAccessing GPA Information:")

    # Step 15: Get the GPA information for one or more of the students using a loop
    # Step 16: Use the get method grab the GPA information
    for student in student_info:
        gpa = student_info[student].get("GPA")
        print(f"{student}'s GPA is {gpa}")

    # Step 17: Print a heading announcing clearing the student registry
    print("\nClearing Student Registry:")

    # Step 18: Use the clear method to remove all students from the dictionary
    student_info.clear()

    # Step 19: Print the dictionary to confirm it's clear
    print("Student Information Dictionary After Clearing:", student_info)

    # Step 20: Include a print statement at the end of the exercise stating the following
    print("\nCompleted by, Your Name Here")

# Calling the main function to execute the program
if __name__ == "__main__":
    main()
