import tkinter as tk
from customtkinter import *
from connection.gerrit_connection import GerritConnection

class LoginUI:
    def __init__(self, root):
        self.connection = None
        self.closed = False
        self.login_window = CTkToplevel(root)
        self.login_window.title("Login")
        self.login_window.minsize(500, 300)
        self.login_window.resizable(width=tk.FALSE, height=tk.FALSE)
        self.login_window.protocol("WM_DELETE_WINDOW", self.on_close)

    def initialize_connection(self, event=None):
        user = {
            'username': self.username_entry.get(),
            'password': self.password_entry.get()
        }
        self.connection = GerritConnection(user)
        self.login_window.destroy()

    def get_login(self):
        self.username_label = CTkLabel(self.login_window, text="Username:", font=("Arial", 16))
        self.username_label.place(relx=0.4, rely=0.3, anchor='e')
        self.username_entry = CTkEntry(self.login_window, font=("Arial", 16))
        self.username_entry.place(relx=0.42, rely=0.3, anchor='w')

        self.password_label = CTkLabel(self.login_window, text="Password:", font=("Arial", 16))
        self.password_label.place(relx=0.4, rely=0.45, anchor='e')
        self.password_entry = CTkEntry(self.login_window, show="*", font=("Arial", 16))
        self.password_entry.place(relx=0.42, rely=0.45, anchor='w')

        login_button = CTkButton(self.login_window, text="Login", command=self.initialize_connection,  font=("Arial", 18))
        login_button.place(relx=0.5, rely=0.85, anchor='center')
        self.login_window.bind('<Return>', self.initialize_connection)
        self.login_window.wait_window(self.login_window)

        return self.connection
    
    def on_close(self):
        self.closed = True
        self.login_window.destroy()
