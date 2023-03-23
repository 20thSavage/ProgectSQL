import sqlite3
# -*- coding: utf-8 -*-
con = sqlite3.connect('server.db',check_same_thread=False)

with con:
    con.execute("""CREATE TABLE IF NOT EXISTS EMPLOYERS(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year TEXT NOT NULL,
            phone_num BIGINT NOT NULL,
            position INTEGER NOT NULL,
            UNIQUE(phone_num))""")



    con.execute("""CREATE TABLE IF NOT EXISTS CLIENT_BASE(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone_num BIGINT NOT NULL,
            UNIQUE(phone_num))""")


sql_insert = "INSERT OR IGNORE INTO EMPLOYERS (name, year, phone_num,position) values(?,?,?,?)"
sql_insert1 = "INSERT OR IGNORE INTO POSITION (name, salary, service) values(?,?,?)"

with con:
    con.executemany(sql_insert,(['Анищенко Игорь Николаевич','28-03-1989',80298982048,2],['Журавлева Жанна Александровна','23-11-1976',80336655489,2],['Дмитревич Ирина Евгеньевна','03-03-1989',80336655431,3],['Васильев Егор Дмитриевич','13-10-2001',80298800533,1],['Ильин Александр Вальеревич','20-09-1994',80297503001,2],['Алиев Денис Викторович','17-03-1992',80296861702,4],['Александровна Екатерина Ильинична','16-11-1994',80293333212,1],['Гаевская Ксения Александровна','01-01-1998',80295143757,2],['Фирсин Игорь Анатольевич','09-12-1976',80291488228,3],['Атрощенко Зинаида Степановна','01-02-1954',80298893134,5]))




with con:
    data = con.execute("SELECT * FROM EMPLOYERS")
    print(data)
    print(data.fetchall())