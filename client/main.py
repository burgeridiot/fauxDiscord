# TODO:
# Convert every variable to camel case,
# Actually get it to log messages and display them (as I can't test this due to school PCs blocking INTERNET CONNECTIONS COMING FROM PYTHON APPS RAHHHH)

# Libraries
import socket
import threading
import window
import mysql.connector

# Creating socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Creating a window through tkinter, and create a confirm variable for binding a button

confirm = window.createLoginWindow()
# Declare variables for the server IP and port
serverIP = ""
serverPort = 0

# Create an array with every message sent, and a string that will contain every message mixed together so the label can display
messagesToDisplay = ""
messagesLogged = ["hi this is a test message \n","helloooooooooooooo\n"]

# Declare a empty variable that will be filled by the name the user types im
nome = ""

# Declare a variable that confirms if it's running
running = True

# Create function that creates the chat window on clicking confirm
def beginChat(placeholder):
   
   # Get some essential variables 
   serverIP = window.ipEntry.get()
   print(serverIP)
   serverPort = int(window.portEntry.get())
   print(serverPort)
   nome = window.usernameEntry.get()
   running = True
   try: 
      sock.sendto(window.yellow + nome  + window.terminalWhite + " has joined the server.".encode(),(serverIP, serverPort))
   except:
      print("Something went wrong.")

   # Close previous window and prepare new window to recieve and send messages
   window.createChatWindow()

   # Create a function to bind to the send button
   def sendMessage(placeholder):
       message = window.yellow + nome  + window.terminalWhite + ": " + window.messageEntry.get()
       sock.sendto(message.encode(),(serverIP,serverPort))
       print(window.messageEntry.get())

   # Create a function to call on threading
   def updateLabel():
       global hasCheckedMessages
       while running:
         window.messageLabel.configure(text=messagesToDisplay)
         print(messagesToDisplay)
         window.messageLabel.update()
   # Create threads to verify messages and update the messages label
   messageCheckThread = threading.Thread(target=message_check)
   messageCheckThread.start()
   labelUpdateThread = threading.Thread(target=updateLabel)
   labelUpdateThread.start()
   # Bind send messages to the button
   window.messageSend.bind("<Button-1>", command=sendMessage) 
   
def message_check():
   while running:
    global messagesToDisplay,hasCheckedMessages
    print(messagesToDisplay)
    msgBytes, ipNotUsed = sock.recvfrom(2048)
    if str.find(msgBytes.decode(),window.yellow + nome) == -1:
       
       messagesLogged.append(msgBytes.decode() + "\n")
       if messagesToDisplay != "":
         messagesToDisplay = ""
       for i in messagesLogged:
        messagesToDisplay = messagesToDisplay + i

confirm.bind("<Button-1>",beginChat)
