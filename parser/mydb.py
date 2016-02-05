import mysql.connector
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read('config.ini')

unix_socket = config.get('database', 'unix_socket')
user = config.get('database', 'username')
password = config.get('database', 'password')
db1 = config.get('database', 'db1')
db2 = config.get('database', 'db2')
def connect(db):
    databaseb = "db" + db
    cnx = mysql.connector.connect( unix_socket = unix_socket, user= username, password= password ,database= database)
    return cnx

