import sqlite3

con = sqlite3.connect('server.db',check_same_thread=False)
def add_new_client(data):
    with con:
        try:
            insert = "INSERT OR IGNORE INTO CLIENT_BASE (name,age,phone_num) values(?,?,?)"
            con.execute(insert,data)
            return True
        except Exception as err:
            return err
def add_employers(data):
    with con:
        try:
            insert = "INSERT OR IGNORE INTO EMPLOYERS (name,year,phone_num,position) values(?,?,?,?)"
            con.execute(insert,data)
            return True
        except Exception as err:
            return err

def add_service(data):
    with con:
        try:
            insert = "INSERT OR IGNORE INTO SERVICE (name,price,time) values(?,?,?)"
            con.execute(insert,data)
            return True
        except Exception as err:
            return err
def return_table(data):
    with con:
        if data == 'EMPLOYERS':
            try:
                data=con.execute("SELECT * FROM EMPLOYER")
                return data
            except Exception as employererr:
                return employererr
        if data == 'SERVICE':
            try:
                data = con.execute("SELECT * FROM SERVICE")
                return data
            except Exception as serviceerr:
                return serviceerr
        if data == 'POSITION':
            try:
                data = con.execute("SELECT * FROM POSITION")
                return data
            except Exception as positionerr:
                return positionerr
        if data == "CLIENT_BASE":
            try:
                data = con.execute("SELECT * FROM CLIENT_BASE")
                return data
            except Exception as clienterr:
                return clienterr
        if data == "ORDERS":
            try:
                data = con.execute("SELECT * FROM ORDERS")
                return data
            except Exception as orderserr:
                return orderserr

def change_table(name,ids,kort):
    with con:
        if name == 'EMPLOYERS':
            try:
                update="UPDATE EMPLOYERS SET name,year,phone_num,position=?,?,?,? WHERE id=?"
                data =(kort,ids)
                cursor.execute(update, data)
                con.commit()
                cursor.close()
                return True
            except Exception as erradd:
                return erradd
        if name == 'CLIENT_BASE':
            try:
                update="UPDATE CLIENT_BASE SET name,age,phone_num=?,?,?, WHERE id=?"
                data =(kort,ids)
                cursor.execute(update, data)
                con.commit()
                cursor.close()
                return True
            except Exception as erradd:
                return erradd
        if name == 'POSITION':
            try:
                update="UPDATE POSITION SET name,salary,service=?,?,? WHERE id=?"
                data =(kort,ids)
                cursor.execute(update, data)
                con.commit()
                cursor.close()
                return True
            except Exception as erradd:
                return erradd
        if name == 'SERVICE':
            try:
                update="UPDATE SERVICE SET name,price,time=?,?,? WHERE id=?"
                data =(kort,ids)
                cursor.execute(update, data)
                con.commit()
                cursor.close()
                return True
            except Exception as erradd:
                return erradd

def comeback_table(data):
    with con:
        try:
            dict_ = {}
            uif=con.execute("SELECT id,name FROM EMPLOYERS,SERVICE,CLIENT BASE")
            dict_.append













add_new_client(('Игорь',18,80293332211))

