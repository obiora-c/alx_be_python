Task = input("Enter your task: ")
Time_Bound = input("Is it time-bound? (yes or no): ").lower()
Priority = input("Priority (high, medium, low): ").lower()


match Priority:
    case "high":
        reminder = f"Reminder: '{Task}' is a high priority task"
        
    case "medium":
        reminder = f"Reminder: '{Task}' is a medium priority task"
        
    case "low":
        reminder = f"Reminder: '{Task}' is a low priority task"
        
    case _:
        reminder = f"Reminder: '{Task}' has an unknown priority task"
        
        
if Time_Bound == "yes":
    reminder += " that requires immediate attention today!"
print(reminder)
