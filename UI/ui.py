import requests
from tkinter import Tk, Label, Entry, Button, messagebox
from .login import Login
from connection.gerrit_connection import GerritConnection

class UI():
    def __init__(self):
        self.login = None
    def run_login(self):
        while True:
            self.login = Login()
            connection = self.login.get_login()
          
            if connection:
                try:
                    connection.connect()
                    break
                except Exception as err:
                    self.show_exception(err)
                
        return connection.user
    
    def show_exception(self,err):
        if isinstance(err, requests.exceptions.HTTPError):
            messagebox.showerror("Login Failed", f"HTTP error occurred: {err}")
        elif isinstance(err, requests.exceptions.ConnectionError):
            messagebox.showerror("Login Failed", f"Error connecting to Gerrit server: {err}")
        elif isinstance(err, requests.exceptions.Timeout):
            messagebox.showerror("Login Failed", f"Request timed out: {err}")
        elif isinstance(err, requests.exceptions.RequestException):
            messagebox.showerror("Login Failed", f"An error occurred: {err}")
        else:
            messagebox.showerror("Login Failed", f"An unexpected error occurred: {err}")
        

        