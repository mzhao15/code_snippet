import sys


with open("sample.sql", "r") as f:
    sqls = f.read()
    for sql in sqls.split(";"):
        sqlcommand = sql.strip()
        print(sqlcommand)
        # print(len(sqlcommand))

my_str = "this is \n the"
new_str = my_str.replace("\n ", "")
print(new_str)

