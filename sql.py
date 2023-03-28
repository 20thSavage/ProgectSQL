import sqlite3 as sl

con = sl.connect('server.db',check_same_thread=False)

with con:
    con.execute("""CREATE TABLE IF NOT EXISTS EMPLOYERS(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year TEXT NOT NULL,
            phone_num BIGINT NOT NULL,
            position INTEGER NOT NULL,
            UNIQUE(phone_num))""")
    con.execute("""CREATE TABLE IF NOT EXISTS POSITION(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            types_service TEXT NOT NULL,
            salary BIGINT NOT NULL,
            service INT NOT NULL)""")
    con.execute("""CREATE TABLE IF NOT EXISTS SERVICE(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price BIGINT NOT NULL,
            time TEXT NOT NULL)""")
    con.execute("""CREATE TABLE IF NOT EXISTS ORDERS(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            client INTEGER NOT NULL,
            service INTEGER NOT NULL,
            employer INTEGER NOT NULL,
            time INTEGER)""")
    con.execute("""CREATE TABLE IF NOT EXISTS CLIENT_BASE(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            phone_num BIGINT NOT NULL,
            UNIQUE(phone_num))""")


sql_insert = "INSERT OR IGNORE INTO EMPLOYERS (name, year, phone_num,position) values(?,?,?,?)"
sql_insert1 = "INSERT OR IGNORE INTO POSITION (name,types_service, salary, service) values(?,?,?,?)"
sql_insert2 = "INSERT OR IGNORE INTO SERVICE (name, price, time) values(?,?,?)"
sql_insert3 = "INSERT OR IGNORE INTO CLIENT_BASE (name,age,phone_num) values(?,?,?)"




with con:
    con.executemany(sql_insert,(['Анищенко Игорь Николаевич','28-03-1989',80298982048,1],['Журавлева Жанна Александровна','23-11-1976',80336655489,2],['Дмитревич Ирина Евгеньевна','03-03-1989',80336655431,3],['Васильев Егор Дмитриевич','13-10-2001',80298800533,4],['Ильин Александр Вальеревич','20-09-1994',80297503001,5],['Алиев Денис Викторович','17-03-1992',80296861702,6],['Александровна Екатерина Ильинична','16-11-1994',80293333212,7],['Гаевская Ксения Александровна','01-01-1998',80295143757,8],['Фирсин Игорь Анатольевич','09-12-1976',80291488228,9],['Атрощенко Зинаида Степановна','01-02-1954',80298893134,10]))
    con.executemany(sql_insert1,(['УЗД','УЗИ почек,УЗИ сердца,УЗИ печени',2400,1],['ЛОР','УЗИ вен',2100,2],['Гематолог','Консультация, Изучение красного костного мозга, Изучение селезенки',1800,3],['Фельдшир','Изучение лимфатических узлов',1900,4],['Эндокринолог','УЗИ щитовидной железы',1600,5],['Остеопад','Консультация, Лечение щитовидной железы',1760,6],['Хирург','Гастропликация,Удаление бандажа желудка,Дистальное кишечное шунтирование',2200,7],['Офтальмолог','Хирургическое лечение лимфостаза, Смена пола',2100,8],['Заведующий отделением','Консультация',2800,9],['Главный врач','Постановка диагноза',2550,10]))
    con.executemany(sql_insert2,(['УЗИ почек',100,'10-00'],['УЗИ вен',90,'10-10'],['Консультация',90,'10-30'],['Изучение лимфатических узлов',70,'11-00'],['УЗИ щитовидной железы',190,'11-00'],['Консультация',150,'11-30'],['Гастропликация',30,'11-30'],['Хирургическое лечение лимфостаза',160,'12-00'],['Консультация',180,'12-00'],['Постановка диагноза',40,'12-00']))
    con.executemany(sql_insert3,(['Муравьёва Джема Арсеньевна',19,80333833737],['Елисеева Яна Эльдаровна',27,80333137786],['Дементьева Устинья Парфеньевна',31,80299929873],['Григорьева Анэля Гордеевна',21,80292212324],['Капустина Альжбета Арсеньевна',35,80297465831],['Петухова Эмилия Семеновна',23,80296677898],['Уварова Эстелла Юлиановна',18,809993909],['Ермакова Марианна Дмитрьевна',41,80337767000],['Евсеев Вячеслав Даниилович',33,80294144578],['Орлов Ким Тарасович',47,80299999342]))
    con.execute("INSERT INTO ORDERS (client,service,employer,time) values(?,?,?,CURRENT_TIMESTAMP)",(0,0,0))


with con:
    data = con.execute("SELECT * FROM EMPLOYERS,POSITION,SERVICE,CLIENT_BASE,ORDERS")
    print(data)
    print(data.fetchall())