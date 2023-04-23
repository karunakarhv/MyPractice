import os
import sqlite3
from sqlite3 import Error

# Password Manager Database
class PasswordMgrDB:
    # Constructor
    def __init__(self):
        self._dirname = os.path.dirname(__file__)
        self.db_file = os.path.join(self._dirname, 'test.db')

    def create_connection(self):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
        except Error as e:
            print(e)

        return conn


    def create_project(conn, project):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = ''' INSERT INTO projects(name,begin_date,end_date)
                VALUES(?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, project)
        conn.commit()
        return cur.lastrowid


    def create_task(conn, task):
        """
        Create a new task
        :param conn:
        :param task:
        :return:
        """

        sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                VALUES(?,?,?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, task)
        conn.commit()
        return cur.lastrowid