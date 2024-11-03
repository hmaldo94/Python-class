import random

def grades():
    grades_list = []
    
    while True:
        user_input = input( "PLease enter the grade or -1 to stop: ")
        if user_input == "-1":
            break
        grades_list.append(user_input)
    print(grades_list)

def remove_lowest(grades_list):
    #"""Remove the lowest grade from the list."""
    print("\nRemoving the lowest grade")
    if grades_list:
        grades_list.pop(grades_list.index(min(grades_list)))
    print(grades_list)

def remove_random(grades_list):
    #"""Remove a random grade from the list."""
    print("\nRemoving a random grade")
    if grades_list:
        grades_list.remove(random.choice(grades_list))
    print(grades_list)

def edit_grade(grades_list):    
    print("\nEditing a grade")
    for index, grades_list in enumerate(grades_list, start=1):
            print(f"{index}. {grades_list}")
        
    while True:
            try:
                edit_index = int(input("Enter the number of the grade you want to edit: ")) - 1
                if edit_index < 0 or edit_index >= len(grades_list):
                    print("Invalid index, please try again.")
                else:
                    new_grade = int(input("Enter the new grade: "))
                    grades_list[edit_index] = new_grade
                    break
            except ValueError:
                print("Please enter a valid integer.")
                print(grades_list)
        # Sort and reverse the list
def sort_reverse(grades_list):
        print("\nSorting and reversing the list")
        grades_list.sort()
        grades_list.reverse()
        print(grades_list)
def total_average(grades_list):
     # Calculate total and average
        total = sum(grades_list)
        average = total / len(grades_list) if grades_list else 0
        print("\nGetting grade Total and Average")
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