import os
from datetime import datetime

# Define the journal file path
journal_file = "journal.txt"

# Function to display the menu
def display_menu():
    print("\n--- Journal App ---")
    print("1. View Journal Entries")
    print("2. Add a New Journal Entry")
    print("3. Exit")

# Function to view journal entries
def view_entries():
    if os.path.exists(journal_file):
        with open(journal_file, 'r') as file:
            entries = file.readlines()
            if entries:
                print("\n--- Your Journal Entries ---")
                for entry in entries:
                    print(entry.strip())
            else:
                print("No journal entries found.")
    else:
        print("No journal entries file found.")

# Function to add a new journal entry
def add_entry():
    entry = input("\nEnter your journal entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(journal_file, 'a') as file:
        file.write(f"{timestamp} - {entry}\n")
    print("Your journal entry has been saved.")

# Main function to run the app
def main():
    while True:
        display_menu()
        choice = input("\nChoose an option: ")

        if choice == '1':
            view_entries()
        elif choice == '2':
            add_entry()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
