import requests
import sqlite3
import hashlib
from Client import Client

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?" 
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    ######
    hashed_pass = hash_password(new_pass)

    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (hashed_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    ###
    hashed_pass = hash_password(password)

    insert_sql = "INSERT INTO clients (username, password) VALUES (?,?)"
    cursor.execute(insert_sql,(username, hashed_pass))
    conn.commit()


def login(username, password):
###############
    hashed_pass = hash_password(password)

    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1"
    
    cursor.execute(select_query, (username, hashed_pass))
    user = cursor.fetchone()

    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False

######################
def strong_password(password, username):
    if len(password) < 8:
        return False
    elif password.isalpha():                # not only characters "abcdtakahd"
        return False
    elif password.isdigit():                # not only digits "12345678"
        return False
    elif password == password.lower():      #not only lowercase "abbljdfisurfh"
        return False
    elif password == password.upper():      #not only uppercase "JDHGKDFEWGD"
        return False
    elif username in password:              # username is not a substring username: "aba"  pass: "12aba3456"
        return False
    else:
        a ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0897654321"
        for character in password:
            if character not in a:          #has a symbol "12BakjJ45!"  - strong password
                return True
        return False


def hash_password(password):
    hash_object = hashlib.sha1()
    hash_object.update(password.encode("utf-8"))    
    hashed_pass = hash_object.hexdigest()
    return hashed_pass
