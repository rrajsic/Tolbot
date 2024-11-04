import requests
import sys
from tkinter import Tk, Label, Entry, Button, messagebox, Radiobutton, StringVar, ttk, BooleanVar
from .login import Login
from connection.gerrit_connection import GerritConnection
from .gerrit__form_ui import GerritFormUI
from Export.MSWord import MSWord

class UI():
    def __init__(self):
        self.login = None
        self.gerrit_ui = None
        self.selected_import_option = None
        self.repositories = None
        
        self.window = Tk()
        self.window.minsize(1200, 800)
        self.window.title("Tolbot")
        self.window.resizable(width=False, height=False)
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_main_window(self, user):
        self.user = user
        self.welcome_label = Label(self.window, text="Welcome to Tolbot", font=("Arial", 20))
        self.welcome_label.place(relx=0.05, rely=0.05, anchor='w')

        self.select_import_label = Label(self.window, text="Select import location", font=("Arial", 16))
        self.select_import_label.place(relx=0.05, rely=0.1, anchor='w')

        self.selected_import_option = StringVar(value="gerrit")

        gerrit_radiobutton = Radiobutton(self.window, text="Gerrit", variable=self.selected_import_option, value="gerrit")
        gerrit_radiobutton.place(relx=0.05, rely=0.15, anchor="w")
        gtms_radiobutton = Radiobutton(self.window, text="GTMS", variable=self.selected_import_option, value="gtms")
        gtms_radiobutton.place(relx=0.05, rely=0.2, anchor="w")

        import_button = Button(self.window, text="Import", command=self.start_import_window, font=("Arial", 14), width=10, height=1)
        import_button.place(relx=0.1, rely=0.25, anchor='center')

        self.separator = ttk.Separator(self.window, orient='horizontal')
        self.separator.place(relx=0.5, rely=0.3, anchor='center', relwidth=0.8)

        export_button = Button(self.window, text="Export", command=self.export, font=("Arial", 14), width=10, height=1)
        export_button.place(relx=0.1, rely=0.35, anchor='center')

        self.window.mainloop()

    
    def export(self):
        suites = None
        tests = None
        repos = None
        for repository in self.repositories:
            suites.append(repository.get_change_files())
            tests.append(repository.get_tests())
            repos.append(repository.get_repo())

        ms_word = MSWord("SP9999-2", "xFT-Cortex")
        # ms_word.create_statistic_page(suites | suites2, tests + tests2)
        for repo, test in zip(repos, tests):
            ms_word.fill_test_data(repo, test)

        ms_word.save()

        self.window.destroy()

    def start_import_window(self):
        if self.selected_import_option.get() == "gerrit":
            self.repositories = self.run_gerrit_form_ui(self.user)
        print("DAAAAAA")
        

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
                
        self.user = connection.user

        
    def run_gerrit_form_ui(self, user):
        gerrit_ui = GerritFormUI(self.window, user)
        self.repositories = gerrit_ui.get_repositories()
            
    
    def on_close(self):
        self.window.destroy()
        sys.exit()
    
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

        

        