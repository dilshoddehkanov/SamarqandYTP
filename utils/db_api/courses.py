import sqlite3


class Courses_db:
    def __init__(self, path_to_db="courses.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_courses(self):
        sql = """
        CREATE TABLE Courses(
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            Course varchar(30),
            InformationUz varchar (500),
            InformationRu varchar (500),
            Photo_id varchar (100),
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, course: str, informationuz: str=None, informationru: str=None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Courses(id, Name, Course, InformationUz, InformationRu) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, course, informationuz, informationru), commit=True)

    def select_all_courses(self):
        sql = """
        SELECT * FROM Courses
        """
        return self.execute(sql, fetchall=True)

    def select_course(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Courses WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_courses(self):
        return self.execute("SELECT COUNT(*) FROM Courses;", fetchone=True)

    def update_course(self, course, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Courses SET Course=? WHERE id=?
        """
        return self.execute(sql, parameters=(course, id), commit=True)

    def update_informationuz(self, informationuz, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Courses SET InformationUz=? WHERE id=?
        """
        return self.execute(sql, parameters=(informationuz, id), commit=True)

    def update_informationru(self, informationru, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Courses SET InformationRu=? WHERE id=?
        """
        return self.execute(sql, parameters=(informationru, id), commit=True)

    def update_photo(self, photo_id, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Courses SET Photo_id=? WHERE id=?
        """
        return self.execute(sql, parameters=(photo_id, id), commit=True)

    def delete_courses(self):
        self.execute("DELETE FROM Courses WHERE TRUE", commit=True)

    def delete_course(self, id):
        sql = f"""
        DELETE FROM Courses WHERE id={id}
        """
        return self.execute(sql, commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
