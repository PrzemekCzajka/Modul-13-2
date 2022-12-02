
from conn_to_db import create_connection

def add_new_car(conn, projects):
   """
   Create a new project into the projects table
   :param conn: the Connection object
   :param projects:
   :return: project id
   """
   sql = '''INSERT INTO projects(nazwa, max_speed, accelerate)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, projects)
   conn.commit()
   return cur.lastrowid

if __name__ == "__main__":
   projects = ("Volvo", "230", "7")
   conn = create_connection("database.db")
   pr_id = add_new_car(conn, projects)
   conn.commit()