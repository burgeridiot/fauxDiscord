
# TODO:
# Convert every variable to camel case,
# Actually get it to log messages and display them (as I can't test this due to school PCs blocking INTERNET CONNECTIONS COMING FROM PYTHON APPS RAHHHH)

# Libraries
import socket
import threading
import customtkinter as tk
tk.set_default_color_theme("dark-blue")
# Defining some essential variables, such as:

#   Window colors,
blurple = "#838fc9"
darkBlurple = "#36427c"
windowWhite = "#ffffff"
#   and chat colors.
yellow = '\033[93m'
terminalWhite = '\033[0m'


# Creating socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Creating a window through tkinter
window = tk.CTk(className='"Faux" Discord')
window.configure(text_color_color="#838fc9")
window.resizable(width=False, height=False)
window.geometry("300x250")
#p1 = tk.PhotoImage(file = 'info.png')
#window.iconphoto(False, p1)

# Defining what buttons it has
usernameLabel = tk.CTkLabel(window,text="   Username   ",text_color = windowWhite)
usernameEntry = tk.CTkEntry(window,width=120,fg_color=darkBlurple,text_color = windowWhite)
ipLabel = tk.CTkLabel(window,text="   IP Address   ",text_color = windowWhite)
portLabel = tk.CTkLabel(window,text="   Port   ",text_color = windowWhite)
spaceForButton = tk.CTkLabel(window,text="",text_color = windowWhite)
ipEntry = tk.CTkEntry(window,width=120,text_color = windowWhite,fg_color=darkBlurple)
portEntry = tk.CTkEntry(window,width=80,text_color = windowWhite,fg_color=darkBlurple)
confirm = tk.CTkButton(window,text="Confirm",text_color = windowWhite,fg_color=darkBlurple)
 
hasCheckedMessages = False # Create a debounce boolean to prevent the label from updating before the messages are actually in the string messagesToDisplay
messagesToDisplay = ""
serverIP = ""
serverPort = 0
messagesLogged = ["hi this is a test message \n","helloooooooooooooo\n"]
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
   running = True
   sock.sendto(automatedJoinMessage.encode(),(serverIP, serverPort))

   # Close previous window and prepare new window to recieve and send messages
   window.destroy()
   window2 = tk.CTk(className = serverIP + ' | "Faux" Discord') # This won't display fully, but just in case...
   window2.resizable(width=False, height=False)
   window2.geometry("600x550")
  
   # Create a function to bind to the send button
   def sendMessage(placeholder):
       message = yellow + nome  + terminalWhite + ": " + messageEntry.get()
       sock.sendto(message.encode(),(serverIP,serverPort))
       print(messageEntry.get())

   

   # Create a function to call on threading
   def updateLabel():
       global hasCheckedMessages
       while running:
         messageLabel.configure(text=messagesToDisplay)
         print(messagesToDisplay)
         messageLabel.update()

   # Set up its components
   messageLabel = tk.CTkLabel(window2,width =580, height=400,fg_color=darkBlurple,text_color = windowWhite)
   messageEntry = tk.CTkEntry(window2,width=580)
   messageSend = tk.CTkButton(window2,text="Send")
   messageLabel.pack()
   messageEntry.pack()
   messageSend.pack()


   # Start checking for messages
   messageCheckThread = threading.Thread(target=message_check)
   messageCheckThread.start()
   labelUpdateThread = threading.Thread(target=updateLabel)
   labelUpdateThread.start()
   messageSend.bind("<Button-1>", command=sendMessage) 
   window2.mainloop()



def message_check():
   while running:
    global messagesToDisplay,hasCheckedMessages
    print(messagesToDisplay)
    msgBytes, ipNotUsed = sock.recvfrom(2048)
    if str.find(msgBytes.decode(),yellow + nome) == -1:
       
       messagesLogged.append(msgBytes.decode() + "\n")
       if messagesToDisplay != "":
         messagesToDisplay = ""
       hasCheckedMessages = True
       for i in messagesLogged:
        messagesToDisplay = messagesToDisplay + i
    
       

       
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
