import sqlite3


class Course_users:
    def __init__(self, path_to_db="course_users.db"):
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

    def create_table_courseusers(self):
        sql = """
        CREATE TABLE CourseUsers (
            id int NOT NULL,
            Course varchar(100) NOT NULL,
            Phone_num varchar(30),
            Full_name varchar(100),
            Address varchar(100),
            Birth_year varchar(20),
            Days varchar(100),
            Day_time varchar(100),
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

    def add_courseuser(self, id: int, course: str, phone_num: str = None, full_name: str = None, address: str = None,
                       birth_year: str = None, days: str = None, day_time: str = None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO CourseUsers(id, Course, Phone_num, Full_name, Address, Birth_year, Days, Day_time) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, course, phone_num, full_name, address, birth_year, days, day_time),
                     commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM CourseUsers
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM CourseUsers WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM CourseUsers;", fetchone=True)

    def update_full_name(self, full_name, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE CourseUsers SET Full_name=? WHERE id=?
        """
        return self.execute(sql, parameters=(full_name, id), commit=True)

    def update_phone_num(self, phone_num, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE CourseUsers SET Phone_num=? WHERE id=?
        """
        return self.execute(sql, parameters=(phone_num, id), commit=True)

    def update_adress(self, address, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE CourseUsers SET Address=? WHERE id=?
        """
        return self.execute(sql, parameters=(address, id), commit=True)

    def update_birth_year(self, birth_year, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE CourseUsers SET Birth_year=? WHERE id=?
        """
        return self.execute(sql, parameters=(birth_year, id), commit=True)

    def update_days(self, days, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE CourseUsers SET Days=? WHERE id=?
        """
        return self.execute(sql, parameters=(days, id), commit=True)

    def update_day_time(self, day_time, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE CourseUsers SET Day_time=? WHERE id=?
        """
        return self.execute(sql, parameters=(day_time, id), commit=True)

    def delete_users(self):
        self.execute("DELETE FROM CourseUsers WHERE TRUE", commit=True)

    def delete_course(self, id):
        sql = f"""
        DELETE FROM CourseUsers WHERE id={id}
        """
        return self.execute(sql, commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
