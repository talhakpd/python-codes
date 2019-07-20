def passwordmanager():
    import pymysql
    db=pymysql.connect("localhost","talha","password","passwordmanager")
    cursor=db.cursor()
    
    sql="select * from pword"
    cursor.execute(sql)
    db.commit()
    results=cursor.fetchall()
    username=input("Enter username for which password is to be found\n")
    db.commit()
    b=False
    for row in results:
        if row[0]==username:
            print("your password is",row[1])
            b=True
    if b==False:
        print("Username not found")

def register():
    import pymysql
    db=pymysql.connect("localhost","talha","password","passwordmanager")
    cursor=db.cursor()
    
    uname=input("Enter username\n")
    s="select * from pword"
    cursor.execute(s)
    results=cursor.fetchall()
    db.commit()
    b=False
    for row in results:
        if row[0]==uname:
            print("Username already exists")
            b=True
    if b==False:
        pwd=input("Enter password\n")
        sql="insert into pword value('%s','%s')"%(uname,pwd)
        cursor.execute(sql)
        db.commit()

while True:
    i=int(input("Enter 1 to register username and password, 2 to retrieve password and any other number to exit\n"))
    if i==1:
        register()
    elif i==2:
        passwordmanager()
    else:
        break
