import sqlite3


def createTable():
  conn = sqlite3.connect("db.db")
  cursor = conn.cursor()
  sqlcommand = "CREATE TABLE users (id Int PRIMARY KEY,time_study String)"
  cursor.execute(sqlcommand)
  conn.close()
  print("OK")
def deleteTable():
  conn = sqlite3.connect("db.db")
  cursor = conn.cursor()
  sqlcommand = "DROP TABLE users"
  cursor.execute(sqlcommand)
  conn.commit()
  conn.close()
  print("OK")
if __name__=="__main__":
  createTable()
  