import sqlite3


class Services_db:
    def __init__(self, path_to_db="services.db"):
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

    def create_table_services(self):
        sql = """
        CREATE TABLE Services(
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            Service varchar(30),
            InformationUz varchar(500),
            InformationRu varchar(500),
            Photo_id varchar(100),
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

    def add_service(self, id: int, name: str, service: str, informationuz: str=None, informationru: str=None, photo_id: str=None):
        # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"

        sql = """
        INSERT INTO Services(id, Name, Service, InformationUz, InformationRu, Photo_id) VALUES(?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, name, service, informationuz, informationru, photo_id), commit=True)

    def select_all_services(self):
        sql = """
        SELECT * FROM Services
        """
        return self.execute(sql, fetchall=True)

    def select_service(self, **kwargs):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
        sql = "SELECT * FROM Services WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def count_courses(self):
        return self.execute("SELECT COUNT(*) FROM Services;", fetchone=True)

    def update_course(self, service, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Services SET Service=? WHERE id=?
        """
        return self.execute(sql, parameters=(service, id), commit=True)

    def update_informationuz(self, informationuz, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Services SET InformationUz=? WHERE id=?
        """
        return self.execute(sql, parameters=(informationuz, id), commit=True)

    def update_informationru(self, informationru, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Services SET InformationRu=? WHERE id=?
        """
        return self.execute(sql, parameters=(informationru, id), commit=True)

    def update_photo(self, photo, id):
        # SQL_EXAMPLE = "UPDATE Users SET email=mail@gmail.com WHERE id=12345"

        sql = f"""
        UPDATE Services SET Photo_id=? WHERE id=?
        """
        return self.execute(sql, parameters=(photo, id), commit=True)

    def delete_services(self):
        self.execute("DELETE FROM Sevices WHERE TRUE", commit=True)

    def delete_service(self, id):
        sql = f"""
        DELETE FROM Services WHERE id={id}
        """
        return self.execute(sql, commit=True)


def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
