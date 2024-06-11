#!/usr/bin/python3
from Subjects import Subject
from StudySessions import StudySession
import sqlite3
from colorama import Back, Fore, Style, init  # type: ignore

# Initialize colorama
init(autoreset=True)

class StudyTrackerCLI:
    def __init__(self):
        Subject.create_table()
        StudySession.create_table()

    def main_menu(self):
        while True:
            print(Fore.CYAN + "------ WELCOME TO THE STUDY TRACKER APP ------")
            print(Fore.CYAN + "Study Tracker Menu")
            print(Fore.CYAN + "1. Add Subject")
            print(Fore.CYAN + "2. View Subjects")
            print(Fore.CYAN + "3. Add Study Session")
            print(Fore.CYAN + "4. View Study Sessions")
            print(Fore.CYAN + "5. Delete Study Session")
            print(Fore.CYAN + "6. Delete Subject")
            print(Fore.CYAN + "7. Exit")
            print(Fore.CYAN + "---------------------------------------------")
            
            choice = input(Fore.YELLOW + "Choose an option: ")

            if choice == '1':
                self.add_subject()
            elif choice == '2':
                self.view_subjects()
            elif choice == '3':
                self.add_study_session()
            elif choice == '4':
                self.view_study_sessions()
            elif choice == '5':
                self.delete_study_session()
            elif choice == '6':
                self.delete_subject()
            elif choice == '7':
                break
            else:
                print(Fore.RED + "Invalid choice, please try again.")

    def add_subject(self):
        try:
            name = input("Enter subject name: ")
            subject = Subject(name)
            subject.save()
            print(Fore.GREEN + f"Success: {name} has been added!")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error adding subject: {e}")

    def view_subjects(self):
        try:
            subjects = Subject.get_all()
            if subjects:
                for subject in subjects:
                    print(Fore.CYAN + f"Name: {subject.name}")
            else:
                print(Fore.YELLOW + "No subjects found.")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error retrieving subjects: {e}")

    def add_study_session(self):
        try:
            subject_id = int(input("Enter subject ID: "))
            date = input("Enter study session date (YYYY-MM-DD): ")
            duration = int(input("Enter duration in minutes: "))
            topics_covered = input("Enter topics to be covered: ")

            study_session = StudySession(subject_id, date, duration, topics_covered)
            study_session.save()
            print(Fore.GREEN + f"Study session added successfully for subject ID {subject_id} on {date}.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter the correct data types.")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error adding study session: {e}")

    def view_study_sessions(self):
        try:
            subject_id = int(input("Enter subject ID to view study sessions: "))
            study_sessions = StudySession.find_by_subject(subject_id)
            if study_sessions:
                print(Fore.CYAN + f"Study sessions for subject ID {subject_id}:")
                for session in study_sessions:
                    print(Fore.CYAN + f"  Date: {session.date}, Duration: {session.duration} minutes, Topics: {session.topics_covered}")
            else:
                print(Fore.YELLOW + f"No study sessions found for subject ID {subject_id}.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter the correct data type for subject ID.")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error retrieving study sessions: {e}")

    def delete_study_session(self):
        try:
            session_id = int(input("Enter study session ID to delete: "))
            study_session = StudySession.find_by_id(session_id)
            if study_session:
                StudySession.delete(session_id)
                print(Fore.GREEN + f"Study session with ID {session_id} has been deleted.")
            else:
                print(Fore.YELLOW + f"Study session with ID {session_id} does not exist.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter the correct session ID.")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error deleting study session: {e}")

    def delete_subject(self):
        try:
            subject_id = int(input("Enter subject ID to delete: "))
            subject = Subject.find_by_id(subject_id)
            if subject:
                Subject.delete(subject_id)
                print(Fore.GREEN + f"Subject with ID {subject_id} has been deleted.")
            else:
                print(Fore.YELLOW + f"Subject with ID {subject_id} does not exist.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter the correct subject ID.")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error deleting subject: {e}")

if __name__ == "__main__":
    cli = StudyTrackerCLI()
    cli.main_menu()

