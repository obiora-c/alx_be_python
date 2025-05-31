
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes or no): ").lower()

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
        
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
        
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority task"
        
        
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
    
print(reminder)