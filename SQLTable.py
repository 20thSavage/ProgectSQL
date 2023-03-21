import sqlite3

con = sqlite3.connect('server.db')

with con:
    con.execute("""
        CREATE TABLE IF NOT EXISTS SMTH (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            year TEXT,
            phone_num BIGINT,
            position INTEGER,
        );
    """)

sql_insert = "INSERT OR IGNORE INTO SMTH (id, name, year, phone_num,position) values(?,?,?,?,?)"

with con:
    con.execute(sql_insert,[1,'Зайцев Егор Андреевич','29/09/1999',80333790666,1])


con.commit()