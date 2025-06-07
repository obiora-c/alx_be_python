
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    # Get user input
    temp_input = input("Enter the temperature to convert: ")
    temp_value = float(temp_input)
    
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    
    if unit == "F":
        celsius = convert_to_celsius(temp_value)
        print(f"{temp_value}°F is {celsius}°C")
        
    elif unit == "C":
        fahrenheit = convert_to_fahrenheit(temp_value)
        print(f"{temp_value}°C is {fahrenheit}°F")
        
    else:
        print("Invalid unit. enter 'C' for Celsius or 'F' for fahrenheit. ")
        
except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")