import sqlite3
con = sqlite3.connect("./_internal/bd/tdm.db")
cursor = con.cursor()
cursor.execute("INSERT INTO tdm VALUES ('Otaivo', 323)")
con.commit()