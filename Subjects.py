from __init__ import CURSOR,CONN
from StudySessions import StudySession
class Subject:
    all=[]
    def __init__(self,name):
        self.name=name
        self.all.append(self)


    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self,name):
        if not isinstance(name,str) or len(name) == 0:
            raise Exception ("Name should be a non-empty string!!")
        self._name=name

        
    @classmethod
    def create_table(cls):
        sql="""
            CREATE TABLE IF NOT EXISTS subjects (
                              id INTEGER PRIMARY KEY,
                              name TEXT
                              )
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql="""
        INSERT INTO subjects (name) VALUES (?)
        """
        CURSOR.execute(sql,(self.name,))
        CONN.commit()

    @classmethod
    def get_all(cls):
        sql="""
        SELECT * FROM subjects
        """
        CURSOR.execute(sql)
        rows=CURSOR.fetchall()
        return [cls(row[1]) for row in rows]


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
            return cls(row[1])
        return None
    
    
    @classmethod
    def delete(cls, subject_id):
        sql = """
        DELETE FROM subjects WHERE id = ?
        """
        CURSOR.execute(sql, (subject_id,))
        CONN.commit()
