from __init__ import CURSOR, CONN
from StudySessions import StudySession

class Subject:
    all = {}

    def __init__(self, student_id, name,id=None):
        self.student_id = student_id
        self.name = name
        self.id=id
        self.all[self.id] = self

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name should be a non-empty string!!")
        self._name = name

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS subjects (
                id INTEGER PRIMARY KEY,
                student_id INTEGER,
                name TEXT NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO subjects (student_id, name) VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.student_id, self.name))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM subjects
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def get_study_sessions(self):
        sql = """
        SELECT * FROM study_sessions WHERE subject_id = (
            SELECT id FROM subjects WHERE name = ?
        )
        """
        CURSOR.execute(sql, (self.name,))
        rows = CURSOR.fetchall()
        return [StudySession(row[1], row[2], row[3], row[4]) for row in rows]

    @classmethod
    def find_by_id(cls, subject_id):
        sql = """
        SELECT * FROM subjects WHERE id = ?
        """
        CURSOR.execute(sql, (subject_id,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None

    @classmethod
    def delete(cls, subject_id):
        sql = """
        DELETE FROM subjects WHERE id = ?
        """
        CURSOR.execute(sql, (subject_id,))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        subject = cls(row[1], row[2])
        subject.id = row[0]
        cls.all[subject.id] = subject
        return subject

