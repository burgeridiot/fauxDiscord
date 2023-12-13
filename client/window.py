import customtkinter as tk
tk.set_default_color_theme("dark-blue")

# Window colors,
blurple = "#838fc9"
darkBlurple = "#36427c"
windowWhite = "#ffffff"
# and chat colors.
yellow = '\033[93m'
terminalWhite = '\033[0m'

def createLoginWindow():
   # Create new window
   window = tk.CTk(className='"Faux" Discord')
   window.configure(text_color="#838fc9")
   window.resizable(width=False, height=False)
   window.geometry("300x250")

   # Defining what buttons it has
   usernameLabel = tk.CTkLabel(window,text="   Username   ",text_color = windowWhite)
   usernameEntry = tk.CTkEntry(window,width=120,fg_color=darkBlurple,text_color = windowWhite)
   ipLabel = tk.CTkLabel(window,text="   IP Address   ",text_color = windowWhite)
   portLabel = tk.CTkLabel(window,text="   Port   ",text_color = windowWhite)
   spaceForButton = tk.CTkLabel(window,text="",text_color = windowWhite)
   ipEntry = tk.CTkEntry(window,width=120,text_color = windowWhite,fg_color=darkBlurple)
   portEntry = tk.CTkEntry(window,width=80,text_color = windowWhite,fg_color=darkBlurple)
   confirm = tk.CTkButton(window,text="Confirm",text_color = windowWhite,fg_color=darkBlurple)

   # Packing everything
   usernameLabel.pack()
   usernameEntry.pack()
   ipLabel.pack()
   ipEntry.pack()
   portLabel.pack()
   portEntry.pack()
   spaceForButton.pack()
   confirm.pack()
   window.mainloop()

def createChatWindow():
   # window.destroy()
   window2 = tk.CTk('"Faux" Discord')
   window2.resizable(width=False, height=False)
   window2.geometry("600x550")
   # Set up its components
   messageLabel = tk.CTkLabel(window2,width =580, height=400,fg_color=darkBlurple,text_color = windowWhite)
   messageEntry = tk.CTkEntry(window2,width=580)
   messageSend = tk.CTkButton(window2,text="Send")

   messageLabel.pack()
   messageEntry.pack()
   messageSend.pack()
   window2.mainloop()
