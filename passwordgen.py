import random
import pymysql

#initial authentication when running program
loginUser = input("username: ")
loginPassword = input("password: ")
db = pymysql.connect(host="192.168.0.191",user=loginUser,password=loginPassword,database="PyPasswordGenerator")
cursor = db.cursor()


#adding login details in db
def addLogin():
    name = input("name: ")
    username = input("username: ")
    passChoice = input("do you wish to generate a new password or enter current password?\n \
    1. generate new(default)\n\n \
        2. enter current password")
    securitykey = input("enter optional securitykey: ")
    
    passChoiceInput = input(": ")
    if passChoiceInput == 1:
        #function to generate password
        char = 'abcdefghijklmnopqrstvwxyzåäö123456789"!¤%&/()=?*><'
        generatedPassword = random.choice(char)

        print("your new password is "+char)
        finalpassword = generatedPassword
    if passChoiceInput == 2:
        print("enter your current password")
        currentpasswordinput= input(": ")
        finalpassword = currentpasswordinput

    
    sql = "INSERT INTO SavedLogin(username,password,securitykey)VALUES (, "+name+", "+finalpassword+", "+securitykey+")"
    try:
        cursor.execute(query=sql)
        db.commit()
    except:
        print("action could not be made")
        db.rollback()

    
addLogin()
#print table details on request
def readTable():
    sql = "SELECT * FROM SavedLogin"
    try:
        cursor.execute(query=sql)
        results = cursor.fetchall()
        for row in results:
            dbusername = row[0]
            dbpassword = row[1]
            dbsecuritykey = row[2]
            print ("username = %s,password = %s,securitykey = %d" % \
                (dbusername, dbpassword, dbsecuritykey ))
    except:
        print("Error: unable to fetch data")

programActive = 1
#show menu options
while programActive == 1:
    print("MENU")
    print("1. add login","\n\n")
    print("2. show logins","\n\n")
    print("3. quit program","\n\n")
    userInput = input(": ")

    if userInput == 1:
        addLogin()
    if userInput == 2:
        readTable()
    if userInput == 3:
        db.close()
        programActive == 0
        exit()
    else:
        print("please choose valid option")