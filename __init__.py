import sqlite3
CONN=sqlite3.connect('students_records.db')
CURSOR=CONN.cursor()


# Ensure tables are created at the start
def initialize_db():
    CURSOR.execute(
        '''CREATE TABLE IF NOT EXISTS subjects (
                              id INTEGER PRIMARY KEY,
                              name TEXT
                              )''')
    CURSOR.execute(
        '''CREATE TABLE IF NOT EXISTS study_sessions (
                              id INTEGER PRIMARY KEY,
                              subject_id INTEGER,
                              date TEXT NOT NULL,
                              duration INTEGER NOT NULL,
                              topics_covered TEXT,
                              FOREIGN KEY(subject_id) REFERENCES subjects(id))'''
    )
    CONN.commit()

initialize_db()
