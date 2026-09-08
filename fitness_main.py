# Khiandra Johnson
# CSCI 471 - Python Programming Assignment: Fitness Tracker Application


#Used for the date when the user inputs it 
from datetime import date

LOG_FILE = "exercise_log.txt"
GOAL_FILE = "weekly_goal.txt"

# Logging an exercise
def log_exercise():
    exercise_type = input("Enter exercise type: ")
    
    try:
        duration = float(input("Enter the duration in minutes: "))
        cal_per_min = float(input("Enter calories burned per minute: "))
    except ValueError:
        print("Pleader enter numbers for duration and calories")
        return
    
    total_calories = duration * cal_per_min
    today = date.today().isoformat()
    
    with open(LOG_FILE, "a") as f:
        f.write(f"{today} | {exercise_type} | {duration} minutes | {total_calories} calories\n")
        
    print(f"Exercise logged successfully for {today}. ")

# Viewing logged exercises from user inputed date
def view_exercise():
    target_date = input("Enter date to view (YYYY - MM - DD): ")
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError: #User has not logged anything yet
        print("No exercises logged yet.")
        return
    
    found = False
    for line in lines:
        if line.startswith(target_date):
            print(line.strip())
            found = True
            
    if not found:
        print(f"No exercises found for {target_date} .")
        
# Setting a goal         
def set_goal():
    try:
        goal = float(input("Enter your weekly calorie-burning goal: "))
    except ValueError: 
        print("Please enter a number: ")
        return
    
    with open(GOAL_FILE, "w") as f: #Used "w" because I only want the latest goal
        f.write(str(goal))
        
    print(f"Weekly goal set to {goal} calories. ")
    
# Tracking progress    
def track_progress():
    try:
        with open(GOAL_FILE, "r") as f:
            goal = float(f.read())
    except FileNotFoundError:
        print("No goal set yet. Please set one first")
        return 
    
    try:
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("No exercises logged yet")
        return 
    
    today = date.today()
    total_calories = 0.0
    
    for line in lines:
        parts = line.strip().split(" | ")
        if len(parts) != 4:
            continue
        
        log_date_text = parts[0]
        calories_text = parts[3].replace("calories", "")
        
        try:
            log_date = date.fromisoformat(log_date_text)
            calories = float(calories_text)
        except ValueError:
            continue
        
        days_ago = (today - log_date).days
        
        if 0<= days_ago < 7:
            total_calories = total_calories + calories
            
    print("\nTotoal calories burned in the last 7 days:", total_calories)
    print("Weekly goal:", goal)
    
    if total_calories >= goal:
        print("You've reached your weekly goal! Great job!")
    else:
        remaining = goal - total_calories
        print("You need", remaining, "more calories to reach your goal. ")
    

# Main Menu - Text-based meni that offers the following options
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
            view_exercise()
        elif choice == "3": 
            set_goal()
        elif choice == "4":
            track_progress()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice")


main()