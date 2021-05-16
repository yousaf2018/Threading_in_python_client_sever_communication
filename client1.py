import socket
import time 
address = "localhost"

port = 5050

c = socket.socket()

c.connect((address,port))
time.sleep(1)
data = c.recv(1024)
print("Enter 1 for account creation identity service")
print("Enter 2 for account authentications")
print("Enter 3 for resource authurization")
check = input()
if check == "1":
    c.send("1".encode("utf-8"))
    data = c.recv(1024)
    print(data.decode("utf-8"))
    name = input("Enter your name---->")
    c.send(name.encode("utf-8"))
    id = input("Enter unique id for your account---->")
    c.send(id.encode("utf-8"))
    r1 = input("Enter 1 if you want use resource R1 or otherwise enter 0---->")
    c.send(r1.encode("utf-8"))
    r2 = input("Enter 1 if you want use resource R2 or otherwise enter 0---->")
    c.send(r2.encode("utf-8"))
    r3 = input("Enter 1 if you want use resource R3 or otherwise enter 0---->")
    c.send(r3.encode("utf-8"))
elif check == "2":
    c.send("2".encode("utf-8"))
    data = c.recv(1024)
    print(data.decode("utf-8"))
    name = input("Enter your name---->")
    c.send(name.encode("utf-8"))
    id = input("Enter id of your account---->")
    c.send(id.encode("utf-8"))
    data = c.recv(1024)
    print(data.decode("utf-8"))
elif check == "3":
    c.send("3".encode("utf-8"))
    data = c.recv(1024)
    print(data.decode("utf-8"))
    id = input("Enter your Id---->")
    c.send(id.encode("utf-8"))
    res = input("Enter 1 for r1,2 for r2,3 for r3--->")
    c.send(res.encode("utf-8"))
    data = c.recv(1024)
    print(data.decode("utf-8"))


