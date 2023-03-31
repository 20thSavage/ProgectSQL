import sqlite3

con = sqlite3.connect('server.db', check_same_thread=False)


def add_new_client(data):
    with con:
        try:
            insert = "INSERT OR IGNORE INTO CLIENT_BASE (name,age,phone_num) values(?,?,?)"
            con.execute(insert, data)
            return True
        except Exception as err:
            return err


def add_employers(data):
    with con:
        try:
            insert = "INSERT OR IGNORE INTO EMPLOYERS (name,year,phone_num,position) values(?,?,?,?)"
            con.execute(insert, data)
            return True
        except Exception as err:
            return err


def add_service(data):
    with con:
        try:
            insert = "INSERT OR IGNORE INTO SERVICE (name,price,time) values(?,?,?)"
            con.execute(insert, data)
            return True
        except Exception as err:
            return err


def return_table(data):
    with con:
        if data == 'EMPLOYERS':
            try:
                data = con.execute("SELECT * FROM EMPLOYERS")
                titile = con.execute("PRAGMA table_info(EMPLOYERS)")
                name = []
                for i in titile:
                    name.append(i[1])
                return data,name
            except Exception as employererr:
                return employererr
        if data == 'SERVICE':
            try:
                data = con.execute("SELECT * FROM SERVICE")
                titile = con.execute("PRAGMA table_info(SERVICE)")
                name = []
                for i in titile:
                    name.append(i[1])
                return data,name
            except Exception as serviceerr:
                return serviceerr
        if data == 'POSITION':
            try:
                data = con.execute("SELECT * FROM POSITION")
                titile = con.execute("PRAGMA table_info(POSITION)")
                name = []
                for i in titile:
                    name.append(i[1])
                return data,name
            except Exception as positionerr:
                return positionerr
        if data == "CLIENT_BASE":
            try:
                data = con.execute("SELECT * FROM CLIENT_BASE")
                titile = con.execute("PRAGMA table_info(CLIENT_BASE)")
                name = []
                for i in titile:
                    name.append(i[1])
                return data,name
            except Exception as clienterr:
                return clienterr
        if data == "ORDERS":
            try:
                data = con.execute("SELECT * FROM ORDERS")
                titile = con.execute("PRAGMA table_info(ORDERS)")
                name = []
                for i in titile:
                    name.append(i[1])
                return data,name
            except Exception as orderserr:
                return orderserr


def change_table(name, ids, kort): # получает name = 'TEXT' ids = integer kort = ()
    with con:
        if name == 'EMPLOYERS':
            try:
                update = f"UPDATE EMPLOYERS SET name='{kort[0]}',year='{kort[1]}',phone_num={kort[2]},position={kort[3]} WHERE id={ids}"
                # ("EMPLOYERS"(TEXT),4(int),('Витя'(TEXT),'1982'(TEXT),337474374(BIGINT),3(int))
                con.execute(update)
                return True
            except Exception as erradd:
                return erradd
        if name == 'CLIENT_BASE':
            try:
                cursor = con.cursor()
                update = f"UPDATE CLIENT_BASE SET name='{kort[0]}',age={kort[1]},phone_num={kort[2]} WHERE id={ids}"
                # ("CLIENT_BASE"(TEXT),4(int),('Витя'(TEXT),24(int),34353553(BIGINT))
                con.execute(update)
                return True
            except Exception as erradd:
                return erradd
        if name == 'ORDERS':
            try:
                cursor = con.cursor()
                update = f"UPDATE ORDERS SET client={kort[0]},service={kort[1]},employer={kort[2]} WHERE id={ids}"
                #("ORDERS"(TEXT),4(int),(4(INT),3(INT),2(INT))
                con.execute(update)
                return True
            except Exception as erradd:
                return erradd
        if name == 'SERVICE':
            try:
                cursor = con.cursor()
                update = f"UPDATE SERVICE SET name='{kort[0]}',price={kort[1]},time='{kort[2]}' WHERE id={ids}"
                #("SERVICE"(TEXT),4(int),('УЗИ'(TEXT),103(BIGINT),'11-30'(TEXT)))
                cursor.execute(update)
                return True
            except Exception as erradd:
                return erradd


def comeback_table():
    with con:
        try:
            all_dicts=[]
            dict_doctor = {}
            dict_client = {}
            dict_service = {}
            select_doctor = con.execute("SELECT id,name FROM EMPLOYERS")
            select_client = con.execute("SELECT id,name FROM CLIENT_BASE")
            select_service = con.execute("SELECT id,name FROM SERVICE")
            for x in select_doctor:
                dict_doctor.update({x[0]: x[1]})
            for x in select_client:
                dict_client.update({x[0]: x[1]})
            for x in select_service:
                dict_service.update({x[0]: x[1]})
        except:
            pass
    all_dicts.append(dict_service)
    all_dicts.append(dict_doctor)
    all_dicts.append(dict_client)
    return all_dicts

#НЕ МЕНЯЙ НАЗВАНИЯ!
def add_z (id):
    with con:
        try:
            add = "INSERT OR IGNORE INTO ORDERS (client,service,employer) values(?,?,?)"
            con.execute(add,id)
            return True
        except Exception as err:
            return err

def del_(table,ids): # запрос нужен в формате table = 'TEXT', ids = int и всё
    with con:
        try:
            if table == 'CLIENT_BASE':
                cursor = con.cursor()
                delete_id = "DELETE FROM CLIENT_BASE WHERE id = ?"
                cursor.execute(delete_id,(ids, ))
                con.commit()
                cursor.close()
                return True
        except Exception as errdel:
            return errdel
        try:
            if table == 'EMPLOYERS':
                cursor = con.cursor()
                delete_id = "DELETE FROM EMPLOYERS WHERE id = ?"
                cursor.execute(delete_id,(ids, ))
                con.commit()
                cursor.close()
                return True
        except Exception as errdel:
            return errdel
        try:
            if table == 'SERVICE':
                cursor = con.cursor()
                delete_id = "DELETE FROM SERVICE WHERE id = ?"
                cursor.execute(delete_id, (ids,))
                con.commit()
                cursor.close()
                return True
        except Exception as errdel:
            return errdel
        try:
            if table == 'ORDERS':
                cursor = con.cursor()
                delete_id = "DELETE FROM ORDERS WHERE id = ?"
                cursor.execute(delete_id, (ids,))
                con.commit()
                cursor.close()
                return True
        except Exception as errdel:
            return errdel

















