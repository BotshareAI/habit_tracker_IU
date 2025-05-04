# Import the csv module - built-in Python library for handling CSV file operations
import csv
import os #standard library module in Python that provides functions for interacting with the operating system

# Define the file path where the habits will be saved and loaded from
csv_file_path = "habits.csv"

# Initialize an empty list to store habits
habits = []

# Function to add a habit to the habits list
def add_habit(habit_name):
    habits.append(habit_name)

# Function to save the list of habits to a CSV file
def save_habits_to_csv():
    # Open the CSV file in write mode ("w") and ensure newlines are handled correctly
    with open(csv_file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Habit Name"])  # Write a header row
        for habit in habits:
            writer.writerow([habit])  # Write each habit in a new row

# Function to load habits from a CSV file
def load_habits_from_csv():
    # Check if the file exists to avoid errors
    if not os.path.exists(csv_file_path):
        print(f"No existing habits file found at {csv_file_path}.")
        return
    
    # Open the CSV file in read mode ("r")
    with open(csv_file_path, mode="r", newline="") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if row:  # Ensure the row is not empty
                habits.append(row[0])  # Each row is a list with one item

# Main program execution starts here
if __name__ == "__main__":
    # Attempt to load existing habits
    load_habits_from_csv()
    
    # Display loaded habits
    if habits:
        print("Loaded habits:")
        for h in habits:
            print(f"- {h}")
    
    # Loop to collect new habits
    while True:
        habit = input("Enter a new habit (or type 'q' to quit): ").strip()
        if habit.lower() == 'q':
            break
        add_habit(habit)
    
    # Save all collected habits to the CSV file
    save_habits_to_csv()
    print(f"Habits successfully saved to {csv_file_path}")
