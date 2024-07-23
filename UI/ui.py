from tkinter import Tk, Label, Entry, Button, messagebox
from .login import Login

class UI():
    def __init__(self):
        self.login_window = None
    def run_login(self):
        self.login_window = Login()

        