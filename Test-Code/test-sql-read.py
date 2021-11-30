import sqlite3

class Database(object):

    def __init__(self, filename):
        self._sqliteConnection = None
        self._cursor = None
        self._filename = filename

    def connect(self):
        try:
            self._sqliteConnection = sqlite3.connect(self._filename)
            self._cursor = self._sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
        # finally:


    def insert_row(self):
        # sqlite_insert_query = """INSERT INTO TEMPLATE
        #                     (SI_NO, RBID, JIRA_ID, DATE_SUBMIT, SVN_REV)
        #                     VALUES
        #                     (60,'1235','test','2019-03-17','r8000')"""
        sqlite_insert_query = """INSERT INTO my_submissions
                            VALUES
                            (NULL, '1235','test','2019-03-17','r8000')"""

        count = self._cursor.execute(sqlite_insert_query)
        self._sqliteConnection.commit()
        print("Record inserted successfully into Sqlite Template table ", self._cursor.rowcount)

    def create_primary_key(self):
        # create a new table with the same column names and types while
        # defining a primary key for the desired column
        sql_query = """
                            PRAGMA foreign_keys=off;
                            BEGIN TRANSACTION;
                            ALTER TABLE my_submissions RENAME TO TEMPLATE_OLD;
                            CREATE TABLE my_submissions (SI_NO TEXT PRIMARY KEY NOT NULL,
                                                    RBID INTEGER,
                                                    JIRA_ID TEXT,
                                                    DATE_SUBMIT TEXT,
                                                    SVN_REV TEXT);

                            INSERT INTO my_submissions SELECT * FROM TEMPLATE_OLD;
                            DROP TABLE TEMPLATE_OLD;
                            COMMIT TRANSACTION;
                            PRAGMA foreign_keys=on;"""
        self._cursor.executescript(sql_query)
        self._sqliteConnection.commit()
        print("Record inserted successfully into Sqlite Template table ", self._cursor.rowcount)

    def delete_row(self):
        sqlite_delete_query = """DELETE FROM TEMPLATE
                                where SI_NO=60"""

        count = self._cursor.execute(sqlite_delete_query)
        self._sqliteConnection.commit()

    def dump_table(self):
        sqlite_select_query = """SELECT * FROM my_submissions"""
        self._cursor.execute(sqlite_select_query)
        data_to_print = self._cursor.fetchall()
        for idx in data_to_print:
            print(idx)

    def clean_up(self):
        if self._cursor:
            self._cursor.close()
            print("The SQLite Cursor object is closed")
        if self._sqliteConnection:
            self._sqliteConnection.close()
            print("The SQLite connection is closed")

if __name__ == "__main__":
    db_read = Database('sqlite.db')
    db_read.connect()
    # db_read.insert_row()
    db_read.create_primary_key()
    # db_read.delete_row()
    db_read.dump_table()
    db_read.clean_up()

