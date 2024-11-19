# import sqlite3
#
#
# class Database:
#     def __init__(self, path_to_db="main.db"):
#         self.path_to_db = path_to_db
#
#     @property
#     def connection(self):
#         return sqlite3.connect(self.path_to_db)
#
#     def execute(
#             self,
#             sql: str,
#             parameters: tuple = None,
#             fetchone=False,
#             fetchall=False,
#             commit=False,
#     ):
#         print(sql)
#         if not parameters:
#             parameters = ()
#         connection = self.connection
#         connection.set_trace_callback(logger)
#         cursor = connection.cursor()
#         data = None
#         cursor.execute(sql, parameters)
#
#         if commit:
#             connection.commit()
#         if fetchall:
#             data = cursor.fetchall()
#         if fetchone:
#             data = cursor.fetchone()
#         connection.close()
#         return data
#
#     @staticmethod
#     def format_args(sql, parameters: dict):
#         sql += " AND ".join([f"{item} = ?" for item in parameters])
#         return sql, tuple(parameters.values())
#
#     @staticmethod
#     def format_args_comma(sql, parameters: dict):
#         sql += ", ".join([
#             f"{item} = ?" for item in parameters
#         ])
#         return sql, tuple(parameters.values())
#
#     def add_user(self, id: int, name: str, email: str = None, language: str = "uz"):
#         # SQL_EXAMPLE = "INSERT INTO Users(id, Name, email) VALUES(1, 'John', 'John@gmail.com')"
#
#         sql = """
#         INSERT INTO users(id, name, email, language) VALUES(?, ?, ?, ?)
#         """
#         self.execute(sql, parameters=(id, name, email, language), commit=True)
#
#     def create_comment(self, user_id, comment):
#
#         sql = """
#         INSERT INTO comments (user_id, comment) VALUES(?, ?)
#         """
#         self.execute(sql, parameters=(user_id, comment), commit=True)
#
#     def select_all_users(self):
#         sql = """
#         SELECT * FROM users
#         """
#         return self.execute(sql, fetchall=True)
#
#     def selects_users(self, **kwargs):
#         sql = "SELECT * FROM users WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=parameters, fetchall=True)
#
#     def select_referals(self, **kwargs):
#         parameters = ()
#         sql = "SELECT * FROM referal"
#         if kwargs:
#             sql += " WHERE "
#             sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=parameters, fetchall=True)
#
#     def update_referal(self, name, quantity):
#         current_quantity_sql = "SELECT quantity FROM referal WHERE name = ?"
#         current_quantity = self.execute(
#             current_quantity_sql, parameters=(name,), fetchone=True
#         )
#
#         if current_quantity:
#             new_quantity = current_quantity[0] + quantity
#             update_sql = "UPDATE referal SET quantity = ? WHERE name = ?"
#             self.execute(update_sql, parameters=(new_quantity, name), commit=True)
#         else:
#             print(f"Referal with name {name} not found.")
#
#     def get_referal(self, name):
#         sql = "SELECT id FROM referal WHERE name = ?"
#         parameters = (name,)
#         return self.execute(sql, parameters=parameters, fetchone=True)
#
#     def select_product_trek_code(self, **kwargs):
#         sql = "SELECT trek_code FROM products WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=parameters, fetchall=True)
#
#     def select_product_arrive_taken(self, **kwargs):
#         sql = "SELECT is_arrived, is_taken FROM products WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=parameters, fetchall=True)
#
#     def update_user(self, phone_number, **kwargs):
#         sql = "UPDATE users SET "
#         sql, parameters = self.format_args_comma(sql, kwargs)
#         sql += " WHERE phone_number = ?"
#         parameters += (phone_number,)
#         return self.execute(sql, parameters=parameters, commit=True)
#
#     def update_user_by_id(self, tg_id, **kwargs):
#         sql = "UPDATE users SET "
#         sql, parameters = self.format_args_comma(sql, kwargs)
#         sql += " WHERE tg_id = ?"
#         parameters += (tg_id,)
#         return self.execute(sql, parameters=parameters, commit=True)
#
#     def update_user_loc(self, latitude, longitude, tg_id):
#         sql = "UPDATE Users SET latitude=?, longitude=? WHERE tg_id=?"
#         parameters = (latitude, longitude, tg_id)
#         return self.execute(sql, parameters=parameters, commit=True)
#
#     def select_user(self, **kwargs):
#         # SQL_EXAMPLE = "SELECT * FROM Users where id=1 AND Name='John'"
#         sql = "SELECT * FROM Users WHERE "
#         sql, parameters = self.format_args(sql, kwargs)
#         return self.execute(sql, parameters=parameters, fetchone=True)
#
#     def delete_users(self):
#         self.execute("DELETE FROM Users WHERE TRUE", commit=True)
#
#     def create_user(
#             self,
#             full_name,
#             phone_number,
#             lang,
#             passport1,
#             passport2,
#             is_active,
#             is_standart,
#             is_kg,
#             id_code,
#             tg_id,
#             image,
#             phone_number2,
#             latitude,
#             longitude,
#             referal_id,
#             types
#     ):
#         sql = "INSERT INTO users(full_name, phone_number, lang, passport1, passport2, is_active, is_standart, is_kg, id_code, tg_id, image, phone_number2, latitude, longitude, referal_id, types) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
#         parameters = (
#             full_name, phone_number, lang, passport1, passport2, is_active, is_standart, is_kg, id_code, tg_id, image,
#             phone_number2,
#             latitude, longitude, referal_id, types)
#         return self.execute(sql, parameters=parameters, commit=True)
#
#     def create_user_referal(
#             self,
#             tg_id,
#             referal_id
#     ):
#         sql = "INSERT INTO users(tg_id, referal_id) VALUES (?, ?)"
#         parameters = (tg_id, referal_id)
#         return self.execute(sql, parameters=parameters, commit=True)
#
#
# def logger(statement):
#     print(
#         f"""
# _____________________________________________________
# Executing:
# {statement}
# _____________________________________________________
# """
#     )

import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    def __init__(self, db_name="cargo_bot_db", user="postgres", password="100", host="localhost", port="5432"):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    @property
    def connection(self):
        return psycopg2.connect(
            dbname=self.db_name,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def execute(
            self,
            sql: str,
            parameters: tuple = None,
            fetchone=False,
            fetchall=False,
            commit=False,
    ):
        print(sql)
        if not parameters:
            parameters = ()
        connection = self.connection
        cursor = connection.cursor(cursor_factory=RealDictCursor)
        data = None
        try:
            cursor.execute(sql, parameters)

            if commit:
                connection.commit()
            if fetchall:
                data = cursor.fetchall()
            if fetchone:
                data = cursor.fetchone()
        except Exception as e:
            print(f"An error occurred: {e}")
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
        return data

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f"{item} = %s" for item in parameters])
        return sql, tuple(parameters.values())

    @staticmethod
    def format_args_comma(sql, parameters: dict):
        sql += ", ".join([f"{item} = %s" for item in parameters])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str, email: str = None, language: str = "uz"):
        sql = """
        INSERT INTO users(id, name, email, language) VALUES(%s, %s, %s, %s)
        """
        self.execute(sql, parameters=(id, name, email, language), commit=True)

    def create_comment(self, user_id, comment):
        sql = """
        INSERT INTO comments (user_id, comment) VALUES(%s, %s)
        """
        self.execute(sql, parameters=(user_id, comment), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)

    def selects_users(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_referals(self, **kwargs):
        sql = "SELECT * FROM referal"
        if kwargs:
            sql += " WHERE "
            sql, parameters = self.format_args(sql, kwargs)
        else:
            parameters = ()
        return self.execute(sql, parameters=parameters, fetchall=True)

    def update_referal(self, name, quantity):
        current_quantity_sql = "SELECT quantity FROM referal WHERE name = %s"
        current_quantity = self.execute(
            current_quantity_sql, parameters=(name,), fetchone=True
        )

        if current_quantity:
            new_quantity = current_quantity['quantity'] + quantity
            update_sql = "UPDATE referal SET quantity = %s WHERE name = %s"
            self.execute(update_sql, parameters=(new_quantity, name), commit=True)
        else:
            print(f"Referal with name {name} not found.")

    def get_referal(self, name):
        sql = "SELECT id FROM referal WHERE name = %s"
        parameters = (name,)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_product_trek_code(self, **kwargs):
        sql = "SELECT trek_code FROM products WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def select_product_arrive_taken(self, **kwargs):
        sql = "SELECT is_arrived, is_taken FROM products WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchall=True)

    def update_user(self, phone_number, **kwargs):
        sql = "UPDATE users SET "
        sql, parameters = self.format_args_comma(sql, kwargs)
        sql += " WHERE phone_number = %s"
        parameters += (phone_number,)
        return self.execute(sql, parameters=parameters, commit=True)

    def update_user_by_id(self, tg_id, **kwargs):
        sql = "UPDATE users SET "
        sql, parameters = self.format_args_comma(sql, kwargs)
        sql += " WHERE tg_id = %s"
        parameters += (tg_id,)
        return self.execute(sql, parameters=parameters, commit=True)

    def update_user_loc(self, latitude, longitude, tg_id):
        sql = "UPDATE Users SET latitude=%s, longitude=%s WHERE tg_id=%s"
        parameters = (latitude, longitude, tg_id)
        return self.execute(sql, parameters=parameters, commit=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execute(sql, parameters=parameters, fetchone=True)

    def delete_users(self):
        self.execute("DELETE FROM Users WHERE TRUE", commit=True)

    def create_user(
            self,
            full_name,
            phone_number,
            lang,
            passport1,
            passport2,
            is_active,
            is_standart,
            is_kg,
            id_code,
            tg_id,
            image,
            phone_number2,
            latitude,
            longitude,
            referal_id,
            types
    ):
        sql = """
        INSERT INTO users(full_name, phone_number, lang, passport1, passport2, 
                          is_active, is_standart, is_kg, id_code, tg_id, image, 
                          phone_number2, latitude, longitude, referal_id, types) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        parameters = (
            full_name, phone_number, lang, passport1, passport2, is_active, is_standart,
            is_kg, id_code, tg_id, image, phone_number2, latitude, longitude, referal_id, types
        )
        return self.execute(sql, parameters=parameters, commit=True)

    def create_user_referal(self, tg_id, referal_id):
        sql = "INSERT INTO users(tg_id, referal_id) VALUES (%s, %s)"
        parameters = (tg_id, referal_id)
        return self.execute(sql, parameters=parameters, commit=True)

    def select_address_options(self):
        sql = """
                SELECT * FROM app_address
                """
        return self.execute(sql, fetchall=True)


def logger(statement):
    print(
        f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
"""
    )
