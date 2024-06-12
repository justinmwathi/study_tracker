# Study Tracker

Study Tracker is a CLI-based application designed to help students track their study sessions and manage their subjects. The application allows users to add, view, and delete subjects as well as log and manage study sessions associated with those subjects.

## Features

- Add new subjects
- View all subjects
- Add study sessions
- View study sessions for a specific subject
- Delete study sessions
- Delete subjects

## Requirements

- Python 3.x
- SQLite3
- Click (for CLI functionality)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/justinmwathi/study_tracker.git
    cd study_tracker
    ```

2. **Install required packages:**

    ```sh
    pip install colorama
    ```

## Usage

1. **Run the CLI application:**

    ```sh
    ./study_tracker.py
    ```

2. **Main Menu:**

    ```
    Study Tracker Menu
    1. Add Subject
    2. View Subjects
    3. Add Study Session
    4. View Study Sessions
    5. Delete Study Session
    6. Delete Subject
    7. Exit
    ```

3. **Add a Subject:**

    - Select option `1` from the main menu.
    - Enter the subject name when prompted.

4. **View Subjects:**

    - Select option `2` from the main menu.
    - The application will display all the subjects.

5. **Add a Study Session:**

    - Select option `3` from the main menu.
    - Enter the student ID, subject ID, date (YYYY-MM-DD), duration (in minutes), and topics covered when prompted.

6. **View Study Sessions:**

    - Select option `4` from the main menu.
    - Enter the subject ID to view all study sessions associated with that subject.

7. **Delete a Study Session:**

    - Select option `5` from the main menu.
    - Enter the study session ID when prompted.

8. **Delete a Subject:**

    - Select option `6` from the main menu.
    - Enter the subject ID when prompted.

## Project Structure

```plaintext
study_tracker/
│
├── __init__.py
├── study_tracker.py
├── Subjects.py
├── StudySessions.py
└── README.md
