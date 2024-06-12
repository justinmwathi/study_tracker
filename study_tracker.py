#!/usr/bin/python3
from Students import Student
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
        Student.create_table()

    def main_menu(self):
        while True:
            print(Fore.CYAN + "------ WELCOME TO THE STUDY TRACKER APP ------")
            print(Fore.CYAN + "Study Tracker Menu")
            print(Fore.CYAN + "1. Add Student")
            print(Fore.CYAN + "2. View Students")
            print(Fore.CYAN + "3. Add Subject")
            print(Fore.CYAN + "4. View Subjects")
            print(Fore.CYAN + "5. Add Study Session")
            print(Fore.CYAN + "6. View Study Sessions")
            print(Fore.CYAN + "7. Update Study Session")
            print(Fore.CYAN + "8. Delete Study Session")
            print(Fore.CYAN + "9. Delete Subject")
            print(Fore.CYAN + "10. Exit")
            print(Fore.CYAN + "---------------------------------------------")
            
            choice = input(Fore.YELLOW + "Choose an option: ")

            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.view_students()
            elif choice == '3':
                self.add_subject()
            elif choice == '4':
                self.view_subjects()
            elif choice == '5':
                self.add_study_session()
            elif choice == '6':
                self.view_study_sessions()
            elif choice == '7':
                self.update_study_session()
            elif choice == '8':
                self.delete_study_session()
            elif choice == '9':
                self.delete_subject()
            elif choice == '10':
                break
            else:
                print(Fore.RED + "Invalid choice, please try again.")




    def add_student(self):
        try:
            name = input("Enter student name: ")
            email = input("Enter student email: ")
            student = Student(name, email)
            student.save()
            print(Fore.GREEN + f"Success: {name} has been added!")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error adding student: {e}")

    def view_students(self):
        try:
            students = Student.get_all()
            if students:
                for student in students:
                    print(Fore.CYAN + f"Student ID: {student.id}, Name: {student.name}, Email: {student.email}")
            else:
                print(Fore.YELLOW + "No students found.")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error retrieving students: {e}")



    def add_subject(self):
        try:
            student_id = int(input("Enter student ID: "))
            name = input("Enter subject name: ")
            subject = Subject(student_id,name)
            subject.save()
            print(Fore.GREEN + f"Success: {name} has been added!")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error adding subject: {e}")

    def view_subjects(self):
        try:
            subjects = Subject.get_all()
            if subjects:
                for subject in subjects:
                    print(Fore.CYAN + f"Subject ID: {subject.student_id} Name: {subject.name}")
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
            sessions = StudySession.get_all()
            if sessions:
                for session in sessions:
                    print(Fore.CYAN + f"STUDY SESSION ID: {session.id}, Subject ID: {session.subject_id}, Date: {session.date}, Duration: {session.duration}, Topics Covered: {session.topics_covered}")
            else:
                print(Fore.YELLOW + "No study sessions found.")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error retrieving study sessions: {e}")




    def update_study_session(self):
        try:
            session_id = int(input("Enter study session ID to update: "))
            date = input("Enter new study session date (YYYY-MM-DD): ")
            duration = int(input("Enter new duration in minutes: "))
            topics_covered = input("Enter new topics to be covered: ")

            study_session = StudySession.find_by_id(session_id)
            if study_session:
                StudySession.update(session_id, date, duration, topics_covered)
                print(Fore.GREEN + f"Study session with ID {session_id} has been updated.")
            else:
                print(Fore.YELLOW + f"Study session with ID {session_id} does not exist.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter the correct session ID.")
        except sqlite3.Error as e:
            print(Fore.RED + f"Error updating study session: {e}")

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

