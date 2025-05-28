import sqlite3
from database import initialize_database
from repository import write_teams
from mlb_api import get_mlb_teams

def main():
    """Main function to initialize the database and create tables."""
    initialize_database()
    start_interface()
    

def start_interface():
    try:
        continue_program = True
        while(continue_program):
            command = input("(UT) Update teams,  (X) Exit: ")

            if(command.lower() == 'ut'):
                teams = get_mlb_teams()
                write_teams(teams)
                if teams:
                    print("Teams fetched successfully.")
                else:
                    print("No teams found or an error occurred.")

            if(command.lower() == 'x' or command.lower() == 'e'):
                print("Quitting the program...")
                continue_program = False
 
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
