import sqlite3

conn = sqlite3.connect("test.db")
print("open")
c = conn.cursor()
sql = '''
    create table company
        (id int primary key  not null,
        name text not null,
        age int not null,
        address char(50),
        salary real);

'''
# do
c.execute(sql)
# commit
conn.commit()
# close
conn.close()
# print("success")
#search
sql = "selevt id,name,address from company"
cursor = c.execute(sql)
for row in cursor:
#insert
sql1 = '''
    insert into company()
    values()
'''