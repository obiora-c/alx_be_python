

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format it as "YYYY-MM-DD HH:MM:SS"
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", formatted_date)
    
    #return curent_date
    
 
def calculate_future_date():
    try:
        # Prompt the user for a number of days
        days_to_add = int(input("Enter number of days to add to the current date: "))
        # Get the current date and time
        current_date = datetime.now()
        # calcualte the future date
        future_date = current_date + timedelta(days=days_to_add)
        # Format it as "YYYY-MM-DD"
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
        
    except ValueError:
        print("please enter a valid integer.")
        
display_current_datetime()  
calculate_future_date()