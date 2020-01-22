import sqlite3


conn = sqlite3.connect('sqlite_file.db')
c = conn.cursor()
my_list = ['a','b','c','d']

c.execute('''CREATE TABLE if not exists usersdata
           (ID INTEGER PRIMARY KEY NULL,
           username           TEXT    NOT NULL,
           EP           TEXT);''')

for i in my_list:
    c.execute("insert into usersdata (username, EP)  values (?,?)",(i,'gold'))

c.execute('SELECT * FROM usersdata ')
print(c.fetchall())
