import sqlite3
import random

connection = sqlite3.connect('test.db')

cur = connection.cursor()



def read_url():
    cur.execute('SELECT website FROM bs')
    for item in cur.fetchall():

     return item[0]

def read_title():
    cur.execute('SELECT title FROM bs')
    for row in cur.fetchall():
         return row[0]

def main():

    print('URL : '+read_url())
    print('ITEM BF : '+read_title())

main()


