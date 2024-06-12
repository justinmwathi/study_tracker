import sqlite3
from __init__ import CURSOR, CONN

class Student:
    all = {}

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        save_sql = """ 
        INSERT INTO students (name, email) VALUES (?,?)
        """
        CURSOR.execute(save_sql, (self.name, self.email))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM students
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        CONN.commit()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, student_id):
        sql = """
        SELECT * FROM students WHERE id=?
        """
        CURSOR.execute(sql, (student_id,))
        row = CURSOR.fetchone()
        CONN.commit()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def delete(cls, student_id):
        sql = """
        DELETE FROM students WHERE id = ?
        """
        CURSOR.execute(sql, (student_id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        student = cls(row[1], row[2])
        student.id = row[0]
        cls.all[student.id] = student
        return student