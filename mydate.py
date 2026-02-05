from datetime import datetime

# Get user name
name = input("Enter your name: ")

# Get current date and time
current_datetime = datetime.now()

# Print welcome message
print(f"Welcome, {name}!")
print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))