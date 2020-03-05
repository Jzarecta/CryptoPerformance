import sqlite3
from cryptocurrencies import cryptocurrencies as cc

con = sqlite3.connect('crypto.db')
con.cursor()

for label in cc:
    try:
        con.execute('CREATE TABLE IF NOT EXISTS %s( id integer PRIMARY KEY, \
        date text NOT NULL, \
        price integer)' %label.replace('-', '_'))
        con.commit()
    except sqlite3.Error as e:
        print(e)
