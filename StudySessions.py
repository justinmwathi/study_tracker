from __init__ import CURSOR, CONN

class StudySession:
    all = {}

    def __init__(self, subject_id, date, duration, topics_covered, id=None):
        self.subject_id = subject_id
        self.date = date
        self.duration = duration
        self.topics_covered = topics_covered
        self.id = id
        if id is not None:
            self.all[id] = self

    @classmethod
    def create_table(cls):
        sql = """
        CREATE TABLE IF NOT EXISTS study_sessions(
            id INTEGER PRIMARY KEY,
            subject_id INTEGER,
            date INTEGER,
            duration INTEGER,
            topics_covered TEXT,
            FOREIGN KEY(subject_id) REFERENCES subjects(id)
        )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
        INSERT INTO study_sessions (subject_id, date, duration, topics_covered) VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.subject_id, self.date, self.duration, self.topics_covered))
        CONN.commit()
        self.id = CURSOR.lastrowid
        self.all[self.id] = self

    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM study_sessions
        """
        CURSOR.execute(sql)
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, session_id):
        sql = """
        SELECT * FROM study_sessions WHERE id = ?
        """
        CURSOR.execute(sql, (session_id,))
        row = CURSOR.fetchone()
        if row:
            return cls.instance_from_db(row)
        return None

    @classmethod
    def find_by_subject(cls, subject_id):
        sql = """
        SELECT * FROM study_sessions WHERE subject_id = ?
        """
        CURSOR.execute(sql, (subject_id,))
        rows = CURSOR.fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def delete(cls, session_id):
        sql = """
        DELETE FROM study_sessions WHERE id = ?
        """
        CURSOR.execute(sql, (session_id,))
        CONN.commit()

    @classmethod
    def update(cls, session_id, date, duration, topics_covered):
        sql = """
            UPDATE study_sessions 
            SET date = ?, duration = ?, topics_covered = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (date, duration, topics_covered, session_id))
        CONN.commit()

    @classmethod
    def instance_from_db(cls, row):
        session = cls(row[1], row[2], row[3], row[4], row[0])
        return session
