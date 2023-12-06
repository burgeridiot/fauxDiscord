
# TODO:
# Convert every variable to camel case,
# Actually get it to log messages and display them (as I can't test this due to school PCs blocking INTERNET CONNECTIONS COMING FROM PYTHON APPS RAHHHH)
# Allow it to send messages
# Fix the theme, it's quite ugly.


# Libraries
import socket
import threading
import tkinter as tk

# Defining some essential variables, such as:

# Window colors,
blurple = "#838fc9"
darkBlurple = "#36427c"
windowWhite = "#ffffff"
# and chat colors.
yellow = '\033[93m'
terminalWhite = '\033[0m'


# Creating socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Creating a window through tkinter
window = tk.Tk(className='"Faux" Discord')
window.configure(bg="#838fc9")
window.resizable(width=False, height=False)
window.geometry("300x200") 

# Defining what buttons it has
usernameLabel = tk.Label(window,text="   Username   ",bg=blurple,fg = windowWhite)
usernameEntry = tk.Entry(window,width=20,bg=darkBlurple,fg = windowWhite)
ipLabel = tk.Label(window,text="   IP Address   ",bg=blurple,fg = windowWhite)
portLabel = tk.Label(window,text="   Port   ",bg=blurple,fg = windowWhite)
spaceForButton = tk.Label(window,text="",fg = windowWhite,bg=blurple)
ipEntry = tk.Entry(window,width=20,fg = windowWhite,bg=darkBlurple)
portEntry = tk.Entry(window,width=10,fg = windowWhite,bg=darkBlurple)
confirm = tk.Button(window,text="Confirm",fg = windowWhite,bg=darkBlurple)


serverIP = ""
serverPort = 0
messagesLogged = []
nome = ""
running = True
automatedJoinMessage = yellow + nome  + terminalWhite + " has joined the server."

def beginChat(placeholder):
   # Get some essential variables 
   serverIP = ipEntry.get()
   print(serverIP)
   serverPort = int(portEntry.get())
   print(serverPort)
   nome = usernameEntry.get()
   sock.bind(("",serverPort))
   running = True
   sock.sendto(automatedJoinMessage.encode(),(serverIP, serverPort))

   # Prepare new window to recieve and send messages
   window2 = tk.Tk(className = serverIP + ' | "Faux" Discord')
   window2.configure(bg ="#838fc9")
   window2.resizable(width=False, height=False)
   window2.geometry("800x600")
  
   # Set up its components
   messageLabel = tk.Label(window2,width =580, height=30, bg = darkBlurple,fg = windowWhite,justify=tk.LEFT)
   messageEntry = tk.Entry(window2,width=580,bg=darkBlurple,fg = windowWhite)
   messageSend = tk.Button(window2,text="Send",fg = windowWhite,bg=darkBlurple)
   messageLabel.pack()
   messageEntry.pack()
   messageSend.pack()
   # Start checking for messages
   messageCheckThread = threading.Thread(target=message_check)
   messageCheckThread.start()
   # Create loop so that it adds messages to the label
   while running:
      newMsg = ""
      for i in messagesLogged:
         newMsg = newMsg + i
      messageLabel.configure(text=newMsg)

def message_check():
   while running:
    msgBytes, ipNotUsed = sock.recvfrom(2048)
    if str.find(msgBytes.decode(),yellow + nome) == -1:
       messagesLogged.append(msgBytes.decode() + "\n")

       
# Pack it all up

usernameLabel.pack()
usernameEntry.pack()
ipLabel.pack()
ipEntry.pack()
portLabel.pack()
portEntry.pack()
spaceForButton.pack()
confirm.pack()
confirm.bind("<Button-1>",beginChat)
window.mainloop()
