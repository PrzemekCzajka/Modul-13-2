
import sqlite3
from sqlite3 import Error
from conn_to_db import create_connection

def update(conn, table, id, **kwargs):
   """
   update nazwa, max_speed, and accelerate of a projects
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   values = tuple(v for v in kwargs.values())
   values += (id, )

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)

if __name__ == "__main__":
   conn = create_connection("database.db")
   update(conn, "projects", 2, max_speed="270")
   update(conn, "projects", 2, accelerate="4")
   conn.close()