# Khiandra Johnson
# CSCI 471 - Python Programming Assignment: Fitness Tracker Application


# Main menu 
#Log an exercise 

def main ():
    while True:
        print("\n======== Fitness Tracker ======")
        print("1. Log an Excercise")
        print("2. View Logged Excercises ")
        print("3. Set Weekly Calorie Goal")
        print("4. Track Weekly Progress")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            print("You picked log excercise")
        elif choice == "2":
            print("You picked view logged excercises")
        elif choice == "3": 
            print("You picked set weekly calorie goal")
        elif choice == "4":
            print("You picked track weekly progress")
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")
        
main()