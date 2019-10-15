import sqlite3
import pprint

TABLE_NAME = 'PIZZA'
DATABASE_SQL = 'C:/Users/dLnnnnnn/Desktop/database.db'


class DataBase:
    def __init__(self, database_sql):
        self.database_sql = database_sql
        self.connect = sqlite3.connect(database_sql)
        self.cursor = self.connect.cursor()

    def create_db(self, table_name):
        sql_table = 'CREATE TABLE {} (ID INTEGER PRIMARY KEY, NAME VARCHAR(50) NOT NULL, PRICE INTEGER);'.format(table_name)
        self.cursor.execute(sql_table)

    def insert_db(self, insert, table_name):
        sql_insert = 'INSERT INTO {} VALUES {};'.format(table_name, insert)
        self.cursor.execute(sql_insert)
        self.connect.commit()

    def select_all(self, table_name):
        select = 'SELECT * FROM {};'.format(table_name)
        self.cursor.execute(select)
        result = self.cursor.fetchall()
        pprint.pprint(result)

    def select_by_id(self, table_name, table_id):
        select_by_id = 'SELECT * FROM {} WHERE ID = {};'.format(table_name,table_id)
        self.cursor.execute(select_by_id)
        result = self.cursor.fetchall()
        print(result)

    def select_all_group_by(self, table_name, sort_by):
        select_group_by = 'SELECT * FROM {} GROUP BY {};'.format(table_name, sort_by)
        self.cursor.execute(select_group_by)
        result = self.cursor.fetchall()
        pprint.pprint(result)

    def close_connect_db(self):
        self.connect.close()


sort_by = 'NAME'
table_id = 3
insert_1 = (1, "Наполи", 145)
insert_2 = (2, "Лигурия", 155)
insert_3 = (3, "Фреш пицца", 160)
insert_4 = (4, "Mushroom pizza", 140)
insert_5 = (5, "Бьянка", 135)
database = DataBase(DATABASE_SQL)
database.create_db(TABLE_NAME)
database.insert_db(insert_1, TABLE_NAME)
database.insert_db(insert_2, TABLE_NAME)
database.insert_db(insert_3, TABLE_NAME)
database.insert_db(insert_4, TABLE_NAME)
database.insert_db(insert_5, TABLE_NAME)
database.select_all(TABLE_NAME)
database.select_by_id(TABLE_NAME, table_id)
database.select_all_group_by(TABLE_NAME, sort_by)
database.close_connect_db()
