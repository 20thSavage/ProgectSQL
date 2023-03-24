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


add_new_client(('Игорь',18,80293332211))

