import random

def grades():
    ##Collect grades from the user.
    grades_list = []
    while True:
        user_input = input("Please enter the grade or -1 to stop: ")
        if user_input == "-1":
            break
        try:
            grade = int(user_input)
            grades_list.append(grade)
        except ValueError:
            print("Please enter a valid grade.")
    print(grades_list)
    return grades_list

def remove_lowest(grades_list):
    ##Remove the lowest grade from the list.
    print("\nRemoving the lowest grade")
    if grades_list:
        grades_list.pop(grades_list.index(min(grades_list)))
    print(grades_list)

def remove_random(grades_list):
    ##Remove a random grade from the list.
    print("\nRemoving a random grade")
    if grades_list:
        grades_list.remove(random.choice(grades_list))
    print(grades_list)

def edit_grade(grades_list):
    ##Edit a grade in the list.
    print("\nEditing a grade")
    while True:
        for index, grade in enumerate(grades_list, start=1):
            print(f"{index}. {grade}")
        try:
            edit_index = int(input("Which grade do you want to edit: ")) - 1
            if edit_index < 0 or edit_index >= len(grades_list):
                print("Please enter a valid grade!")
            else:
                new_grade = int(input("Enter the new grade: "))
                grades_list[edit_index] = new_grade
                break
        except ValueError:
            print("Please enter a valid grade.")
    print(grades_list)

def sort_reverse(grades_list):
    ##Sort and reverse the grades list.
    print("\nSorting and reversing the list")
    grades_list.sort()
    grades_list.reverse()
    print(grades_list)

def total_average(grades_list):
    ##Calculate and print the total and average of the grades.
    total = sum(grades_list)
    average = total / len(grades_list) if grades_list else 0
    print("\nGetting Grade Total and Average")
    print("Total:", total)
    print("Average:", average)

def main():
    grades_list = grades()
    remove_lowest(grades_list)
    remove_random(grades_list)
    edit_grade(grades_list)
    sort_reverse(grades_list)
    total_average(grades_list)
    print("\nCompleted by, Hector Maldonado")

if __name__ == "__main__":
    main()
