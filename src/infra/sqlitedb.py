"""Sqlitedb."""
import sqlite3
import random
from typing import Union
from src.domain.interfaces import DbInterface
import logging


class DbSqlite(DbInterface):
    """DBSQlite."""

    def __init__(self, db_name: str = 'db') -> None:
        """Construct."""
        DbInterface.__init__(self)
        self.db_name = db_name

    def create_table(self) -> None:
        """Create Table if NOR exists."""
        query = """
            CREATE TABLE IF NOT EXISTS  COINS(
                USER_ID INTEGER NOT NULL,
                USER_NAME TEXT NOT NULL,
                COIN TEXT NOT NULL,
                SYMBOL TEXT NOT NULL,
                VALOR_MIN VARCHAR,
                VALOR_MAX VARCHAR,
                DATA TEXT NOT NULL
            )
        """

        conn = sqlite3.connect(self.db_name + '.sqlite')
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.close()

    def validate_table_register(self) -> bool:
        """Validate the existence of register in the table created."""
        query = """
            SELECT DISTINCT USER_ID FROM COINS
        """

        conn = sqlite3.connect(self.db_name + '.sqlite')
        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        if rows:
            return True
        else:
            return False

    def validate_user_existence(self, user_name: str) -> any:
        """Validate user existence on the database.

        Parameters
        ----------
        user_name: str
        symbol: str
        """
        select_query = f"""
            SELECT USER_ID, USER_NAME, SYMBOL
            FROM COINS
            WHERE USER_NAME == '{user_name}'
        """

        conn = sqlite3.connect(self.db_name + '.sqlite')
        cursor = conn.cursor()
        cursor.execute(select_query)
        rows = cursor.fetchall()
        if rows:
            cursor.close()
            return rows
        else:
            cursor.close()
            return None

    def validate_register_existence(self, user_name: str, symbol: str) -> bool:
        """Validate user existence on the database.

        Parameters
        ----------
        user_name: str
        symbol: str
        """
        select_query = f"""
            SELECT USER_ID, USER_NAME, SYMBOL
            FROM COINS
            WHERE USER_NAME == '{user_name}' and SYMBOL == '{symbol}'
        """

        conn = sqlite3.connect(self.db_name + '.sqlite')
        cursor = conn.cursor()
        cursor.execute(select_query)
        rows = cursor.fetchall()
        if rows:
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def get_user_id(self, user_name: str) -> int:
        """Get user id.

        Get the same user_id for the same user_name and symbol
        or get a new user_id for a new tuple user_name and symbol.

        Parameters
        ----------
        user_name: str
        symbol: str
        """
        val = self.validate_table_register()
        if val is False:
            user_id = DbSqlite.get_random_user_id()
            return user_id

        validation = self.validate_user_existence(user_name)

        if validation is not None:
            user_id = validation[0][0]
            return user_id

        else:
            select_query = """
                SELECT DISTINCT USER_ID FROM COINS
            """
            conn = sqlite3.connect(self.db_name + '.sqlite')
            cursor = conn.cursor()
            cursor.execute(select_query)
            rows = cursor.fetchall()
            unique_ids = [i[0] for i in rows]
            user_id = DbSqlite.get_random_user_id(unique_ids)
            cursor.close()
            return user_id

    def insert_values(self, user_id: str, user_name: str, coin: str,
                      symbol: str, valor_min: Union[int, float],
                      valor_max: Union[int, float], date: str) -> None:
        """Insert values in the table.

        Parameters
        ----------
        user_id: str
        """
        insert_query = f"""
            INSERT INTO COINS (
                USER_ID, USER_NAME, COIN, SYMBOL, VALOR_MIN, VALOR_MAX, DATA)
            VALUES (
                '{user_id}', '{user_name}', '{coin}', '{symbol}',
                {valor_min}, {valor_max}, '{date}')
        """

        validation = self.validate_register_existence(user_name, symbol)
        if validation:
            raise Exception('This register already exist.')
        else:
            print("Insert Query...")
            logging.info(insert_query)
            conn = sqlite3.connect(self.db_name + '.sqlite')
            cursor = conn.cursor()
            cursor.execute(insert_query)
            conn.commit()
            cursor.close()

    def select(self, user_name: str = None, user_id: str = None,
               all: bool = False) -> None:
        """Select data from the database.

        Parameters
        ----------
        user_name: str, default=None
        user_id: str, default=None
        all: bool, default=False
        """
        if all:
            select_query = f"""
                SELECT * FROM COINS
            """
        else:
            if user_name is None and user_id is None:
                raise ValueError(f"You must pass either the UserName"
                                 f"or UserID. Or even pass all as True")

            colum = 'USER_NAME' if user_name is not None else 'USER_ID'
            filter_by = user_name if user_name is not None else user_id
            select_query = f"""
                SELECT * FROM COINS
                WHERE {colum} == '{filter_by}'
            """

        print(select_query)
        conn = sqlite3.connect(self.db_name + '.sqlite')
        cursor = conn.cursor()
        cursor.execute(select_query)
        rows = cursor.fetchall()
        cursor.close()
        output = DbSqlite.format_select_output(rows)
        return output

    def delete(self, user_name: str, symbol: str = None) -> None:
        """Delete register from the database.

        Parameters
        ----------
        user_name: str
        symbol: str
        """
        if symbol is None:
            delete_query = f"""
                DELETE FROM COINS
                WHERE USER_NAME == '{user_name}'
            """
        else:
            delete_query = f"""
                DELETE FROM COINS
                WHERE USER_NAME == '{user_name}' and SYMBOL == '{symbol}'
            """
        print(delete_query)
        conn = sqlite3.connect(self.db_name + '.sqlite')
        cursor = conn.cursor()
        cursor.execute(delete_query)
        conn.commit()
        cursor.close()

    def update(self, user_name: str, new_user_name: str) -> None:
        """Update register of a user.

        Parameters
        ----------
        user_name: str
        new_user_name: str
        """
        val = self.validate_user_existence(user_name=user_name)
        if val is None:
            raise ValueError(f"The user '{user_name}' does not exist.")

        update_query = f"""
            UPDATE COINS
            SET USER_NAME = '{new_user_name}'
            WHERE USER_NAME = '{user_name}'
        """
        print(update_query)
        conn = sqlite3.connect(self.db_name + '.sqlite')
        cursor = conn.cursor()
        cursor.execute(update_query)
        conn.commit()
        cursor.close()

    @staticmethod
    def format_select_output(data: list) -> dict:
        """Format the output of sqlite3.connect.cursor.fetchall().

        Parameters
        ----------
        data: list
        """
        colunas = [
            'USER_ID',
            'USER_NAME',
            'COIN',
            'SYMBOL',
            'VALOR_MIN',
            'VALOR_MAX',
            'DATA'
        ]

        final_dict = {}
        for index, rows in enumerate(data):
            novo_dict = {}

            for coluna, row in zip(colunas, rows):
                novo_dict[coluna] = row

            final_dict[index] = novo_dict

        return final_dict

    @staticmethod
    def get_random_user_id(unique_ids: list = None) -> int:
        """Return the user_id.

        Parameters
        ----------
        unique_ids: list
            unique ids which already exist
        """
        if unique_ids is None:
            user_id = random.randint(1, 10000)
            return user_id
        else:
            user_id = unique_ids[0]
            while user_id in unique_ids:
                user_id = random.randint(1, 10000)
            return user_id
