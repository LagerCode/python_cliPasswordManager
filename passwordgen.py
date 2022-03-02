import random
import mysql.connector
import time
import getpass

#initial authentication when running program
loginUser = input("username: ")
loginPassword = getpass.getpass("password: ")
try:
    dbconn = mysql.connector.connect(host="192.168.0.191",
    user=loginUser,
    password=loginPassword,
    database="PyPasswordGenerator")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Invalid login")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Connection to Database could not be found")
  else:
    print(err)
else:
  dbconn.close()

dbconn.reconnect()
cursor = dbconn.cursor()


#adding login details in db
def addLogin():
    name = input("name: ")
    username = input("username: ")
    securitykey = input("enter optional securitykey: ")
    
    
    char = 'abcdefghijklmnopqrstvwxyzåäö123456789"!¤%&/()=?*><'
    for i in range(15):
        generatedPassword += random.choice(char)
        print("your new password is "+generatedPassword)
    finalpassword = generatedPassword
    
    add_loginDetails = ("INSERT INTO SavedLogin "
                        "(username, password, securitykey, name) "
                        "VALUES (%s, %s, %s, %s)")
    data_loginDetails = (username, finalpassword, securitykey, name)
    cursor.execute(add_loginDetails, data_loginDetails)
    dbconn.commit()
    cursor.close()
    dbconn.close()


#print table details on request
def readTable():
    query = ("SELECT * FROM SavedLogin")
    cursor.execute(query)
    
    
    for row in cursor:
            dblogin_id = row[0]
            dbusername = row[1]
            dbpassword = row[2]
            dbsecuritykey = row[3]
            dbname = row[4]
            print ("login_id = %s,\nusername = %s,\npassword = %s,\nsecuritykey = %s,\nname = %s\n\n\n" % \
                (dblogin_id, dbusername, dbpassword, dbsecuritykey, dbname))


programActive = 1
#show menu options
def menu():
    while programActive == 1:
        print("MENU")
        print("1. add login","\n")
        print("2. show logins","\n")
        print("3. quit program","\n\n")
        userInput = input(": ")

        if userInput == '1':
            addLogin()
            userInput = input("enter any key to continue")
            menu()
        if userInput == '2':
            readTable()
            userInput = input("enter any key to continue")
            menu()
        if userInput == '3':
            dbconn.close()
            programActive == 0
            exit()
        else:
            print("please choose valid option")
            time.sleep(2)
menu()