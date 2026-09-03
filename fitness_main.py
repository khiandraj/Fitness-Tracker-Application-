# Khiandra Johnson
# CSCI 471 - Python Programming Assignment: Fitness Tracker Application


# Main Menu - Text-based meni that offers the following options

from datetime import date

LOG_FILE = "exercise_log.txt"

def log_exercise():
    exercise_type = input("Enter exercise type: ")
    
    try:
        duration = float(input("Enter the duration in minutes: "))
        cal_per_min = float(input("Enter calories burned per minute: "))
    except ValueError:
        print("Pleader enter numbers for duration and calories")
        return
    
    total_calories = duration * cal_per_min
    today = date.today().isoformat
    
    with open(LOG_FILE, "a") as f:
        f.write(f"{today} | {exercise_type} | {duration} minutes | {total_calories} calories\n")
        
    print(f"Exercise logged successfully for {today}. ")





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
            log_exercise()
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