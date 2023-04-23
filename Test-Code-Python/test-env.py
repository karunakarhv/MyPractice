import os
test = os.environ.get("DB_USERNAME_PYTEST")
print(test, type(test))


string_to = "DRIVER=ODBC Driver 17 for SQL Server;SERVER='tcp:172.16.1.91';DATABASE='TimeTarget_PublicApiAutoTest';UID='hfapptest';PWD='kit.trawl.door1'"
new_str = string_to.replace("'",'')
print(new_str)