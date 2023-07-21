import sqlite3
import hashlib

conn = sqlite3.connect("userdata.db")
cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS userdata (
    id INTEGER PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
)""")

username1, password1 = "Mikey", hashlib.sha256("Testing".encode()).hexdigest()
username2, password2 = "Michelle", hashlib.sha256("password".encode()).hexdigest()
username3, password3 = "Marvin", hashlib.sha256("passw3rd!".encode()).hexdigest()
username4, password4 = "Ella", hashlib.sha256("p4s$weRd".encode()).hexdigest()
username5, password5 = "Harold", hashlib.sha256("Tested".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username1,password1))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username2,password2))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username3,password3))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username4,password4))
cur.execute("INSERT INTO userdata (username, password) VALUES(?, ?)", (username5,password5))

conn.commit()

#SQL injection protection due to prepared statements & w/ passwords stored as hash values, they aren't too vuln
#Encrypt the comm