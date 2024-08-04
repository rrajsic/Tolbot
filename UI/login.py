import sys
from tkinter import *
import tkinter.messagebox as messagebox
from connection.gerrit_connection import GerritConnection

class Login:
    def __init__(self):
        self.connection = None

        self.login_window = Tk()
        self.login_window.minsize(900, 600)
        self.login_window.resizable(width=FALSE, height=FALSE)
        self.login_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def initialize_connection(self, event=None):
        user = {
            'username': self.username_entry.get(),
            'password': self.password_entry.get()
        }
        self.connection = GerritConnection(user)

        self.login_window.destroy()

    def get_login(self):
        # Create and place the username label and entry
        self.username_label = Label(self.login_window, text="Username:")
        self.username_label.place(relx=0.5, rely=0.4, anchor='e')

        self.username_entry = Entry(self.login_window)
        self.username_entry.place(relx=0.5, rely=0.4, anchor='w')

        # Create and place the password label and entry
        self.password_label = Label(self.login_window, text="Password:")
        self.password_label.place(relx=0.5, rely=0.5, anchor='e')

        self.password_entry = Entry(self.login_window, show="*")  # Show asterisks for password
        self.password_entry.place(relx=0.5, rely=0.5, anchor='w')

        # Create and place the login button
        login_button = Button(self.login_window, text="Login", command=self.initialize_connection)
        login_button.place(relx=0.5, rely=0.6, anchor='center')

        self.login_window.bind('<Return>', self.initialize_connection)
        self.login_window.mainloop()

        return self.connection
    
    def on_close(self):
        self.login_window.destroy()
        sys.exit()
