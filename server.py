import socket
from threading import Thread
import time
import mysql.connector

#create a class that extends/inherits from Thread class
class MyThread(Thread):
    #create a constructor for our class,
    #counter is just a variable to show how can we take
    # aurguments for our thread
    def __init__(self, client):
        #class the parent constructor that will make sure
        # a separate thread is created, when called
        Thread.__init__(self)
        #save the counter parameter, so that we can use
        #it later
        self.client=client
        #override the run function of the Thread class
    def run(self):
        #The following code will be replaced with your
        #logic. It is just to show some work is being
        #done by this thread. It is just waiting for 1
        # second at each iteration untill we reach the
        self.client.send("Sir what kind of service can i provide to you?".encode("utf-8"))
        data = self.client.recv(1024)
        data = data.decode("utf-8")
        print(data)
        
        if data == "1":
            print("Thanks Sir for showing interest in account opening")
            self.client.send("Please provide your details like name,id,resouces you want to consume".encode("utf-8"))
            name = self.client.recv(1024)
            name = name.decode("utf-8")
            id = self.client.recv(1024)
            id = id.decode("utf-8")
            r1 = self.client.recv(1024)
            r1 = r1.decode("utf-8")
            r2 = self.client.recv(1024)
            r2 = r2.decode("utf-8")
            r3 = self.client.recv(1024)
            r3 = r3.decode("utf-8")
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="a simple identity service"
            )

            mycursor = mydb.cursor()

            sql = "INSERT INTO users_record (name, id,r1,r2,r3) VALUES (%s, %s,%s,%s,%s)"
            val = (name,id,r1,r2,r3)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "Congratualtions for new account in our company")
            
        elif data == "2":
            print("Well Come to Authenication services")
            self.client.send("Please provide name and id for authentications".encode("utf-8"))
            name1 = self.client.recv(1024)
            name1 = name1.decode("utf-8")
            id1 = self.client.recv(1024)
            id1 = id1.decode("utf-8")
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="a simple identity service"
            )

            mycursor = mydb.cursor()

            sql = """SELECT * FROM users_record WHERE id = %s and name = %s"""
            mycursor.execute(sql,(id1,name1,))
            
            myresult = mycursor.fetchall()
            if len(myresult) == 1:
                self.client.send("You are validated by server".encode("utf-8"))
            else:
                self.client.send("Sorry there may be error in your Name or Id".encode("utf-8"))
                
        elif data == "3":
            print("Well Come to Authurization of resources")
            self.client.send("Please provide Id and Resource name like r1,r2,r3 for authurization".encode("utf-8"))
            id1 = self.client.recv(1024)
            id1 = id1.decode("utf-8")
            res = self.client.recv(1024)
            res = res.decode("utf-8")
            
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            database="a simple identity service"
            )

            mycursor = mydb.cursor()

            sql = """SELECT * FROM users_record WHERE id = %s"""
            mycursor.execute(sql,(id1,))
            res = int(res)
            myresult = mycursor.fetchall()
            if myresult[0][res+1] == 1:
                self.client.send("You are authurized to use provided resource".encode("utf-8"))
            else:
                self.client.send("You have no access to this resources".encode("utf-8"))
            print(myresult)


def main():
    Address = "localhost"

    port = 5050

    s = socket.socket()

    s.bind((Address,port))

    s.listen(5)
    print("Listening for client")
    while True:
        c,addr = s.accept()
        #Create object for our thread class
        thread=MyThread(c)
        #thread.run()
        #if you start the thread using run() function, it
        #will be executed on the main thread as normal
        #function. Never use the run() function your self
        #rather call the start(), it will create a separate
        # thread, and there it will call the run function
        thread.start()
if __name__=='__main__':
    main()

