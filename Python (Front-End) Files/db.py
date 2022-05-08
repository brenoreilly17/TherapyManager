from Project.therapy_dbconfig import Config
import mysql.connector

class Database(object):
    #Initializes the database connection
    def __init__(self):
        self.cnx = None
        self.connect()

    #Opens the connection to the database
    def connect(self):
        self.cnx = mysql.connector.connect(user=Config.MYSQL_DATABASE_USER,
                                      password=Config.MYSQL_DATABASE_PASSWORD,
                                      host=Config.MYSQL_DATABASE_HOST,
                                      database=Config.MYSQL_DATABASE_SCHEMA,
                                      port=Config.MYSQL_DATABASE_PORT)

    #Closes the connection to the database
    def disconnect(self):
        self.cnx.close()

    #Executes the statement and then returns the result 
    #Statement - SQL Query
    #Vars - List of variables values for the query
    """ Executes the statement and then returns the result
        Statement - SQL Query
        Vars - List of variables values for the query
        Returns a list as a result """
    def query(self, statement, vars=""):
        cur = self.cnx.cursor()
        if vars:
            cur.execute(statement, vars)
        else:
            cur.execute(statement)

        result = cur.fetchall()
        cur.close()

        return result

    """ Executes the statement and then returns the first row from the result
        Statement - SQL Query
        Vars - List of variables values for the query """
    def query_one(self, statement, vars=""):
        cur = self.cnx.cursor()

        if vars:
            cur.execute(statement, vars)
        else:
            cur.execute(statement)

        result = cur.fetchone()
        cur.close()
        return result

    """ Executes the statement (insert, update, or delete)
        Statement - SQL Query
        Vars - List of variables values for the query
        Does not return anything """
    def execute(self, statement, vars):
        cur = self.cnx.cursor()

        cur.execute(statement, vars)

        self.cnx.commit()
        cur.close()

        return None

    """ Executes the insert statement and returns the generated key from the insert.
        Statement - SQL Query
        Vars - List of variables values for the query
        Returns the generated key """
    def insert_get_generated_key(self, statement, vars):
        cur = self.cnx.cursor()

        cur.execute(statement, vars)
        lastrowid = cur.lastrowid
        self.cnx.commit()
        cur.close()

        return lastrowid
