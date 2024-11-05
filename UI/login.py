import sys
from tkinter import *
import tkinter.messagebox as messagebox
from connection.gerrit_connection import GerritConnection

class Login:
    def __init__(self, root):
        self.connection = None
        self.closed = False
        self.login_window = Toplevel(root)
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
        self.username_label = Label(self.login_window, text="Username:", font=("Arial", 14))
        self.username_label.place(relx=0.5, rely=0.4, anchor='e')

        self.username_entry = Entry(self.login_window, font=("Arial", 14))
        self.username_entry.place(relx=0.52, rely=0.4, anchor='w')

        # Create and place the password label and entry
        self.password_label = Label(self.login_window, text="Password:", font=("Arial", 14))
        self.password_label.place(relx=0.5, rely=0.5, anchor='e')

        self.password_entry = Entry(self.login_window, show="*", font=("Arial", 14))  # Show asterisks for password
        self.password_entry.place(relx=0.52, rely=0.5, anchor='w')

        # Create and place the login button
        login_button = Button(self.login_window, text="Login", command=self.initialize_connection,  font=("Arial", 20))
        login_button.place(relx=0.5, rely=0.8, anchor='center')

        self.login_window.bind('<Return>', self.initialize_connection)
        self.login_window.wait_window(self.login_window)

        return self.connection
    
    def on_close(self):
        self.closed = True
        self.login_window.destroy()
