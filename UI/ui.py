import requests
import sys
from tkinter import Tk, Label, Entry, Button, messagebox, Radiobutton, StringVar, ttk, BooleanVar, Toplevel
import customtkinter
from .login import Login
from connection.gerrit_connection import GerritConnection
from Export.MSWord import MSWord
from Repository.Gerrit.GerritRepository import GerritRepository

class UI():
    def __init__(self):
        self.login = None
        self.gerrit_ui = None
    
        self.repositories = None
        
        self.root = customtkinter.CTk()
        self.root.minsize(800, 800)
        self.root.title("Tolbot")
        self.root.resizable(width=False, height=False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def start_main_window(self, user):
        self.user = user
        self.welcome_label = customtkinter.CTkLabel(self.root, text=f"Hi, {self.user['username']}!", font=("Arial", 22))
        self.welcome_label.place(relx=0.05, rely=0.05, anchor='w')

        self.team_name_label = customtkinter.CTkLabel(self.root, text="Team name:", font=("Arial", 16))
        self.team_name_label.place(relx=0.3, rely=0.05, anchor='w')

        self.team_name_entry = customtkinter.CTkEntry(self.root, font=("Arial", 16))
        self.team_name_entry.place(relx=0.45, rely=0.05, anchor='w')

        self.sp_name_label = customtkinter.CTkLabel(self.root, text="SP name:", font=("Arial", 16))
        self.sp_name_label.place(relx=0.3, rely=0.1, anchor='w')

        self.sp_name_entry = customtkinter.CTkEntry(self.root, font=("Arial", 16))
        self.sp_name_entry.place(relx=0.45, rely=0.1, anchor='w')

        self.separator_1 = ttk.Separator(self.root, orient='horizontal')
        self.separator_1.place(relx=0.5, rely=0.15, anchor='center', relwidth=0.8)

        export_button = customtkinter.CTkButton(self.root, text="Export", command=self.export, font=("Arial", 22))
        export_button.place(relx=0.45, rely=0.95, anchor='center')

        self.create_gerrit_widgets()

    def create_gerrit_widgets(self):
        server_values = ["***REMOVED***"]

        # First repository info

        self.number_label_1 = customtkinter.CTkLabel(self.root, text="1", font=("Arial", 18))
        self.number_label_1.place(relx=0.05, rely=0.2, anchor='w')

        self.server_label_1 = customtkinter.CTkLabel(self.root, text="Server:", font=("Arial", 16))
        self.server_label_1.place(relx=0.15, rely=0.25, anchor='w')

        self.server_entry_1 =  customtkinter.CTkComboBox(self.root, values=server_values, width = 300, font=("Arial", 14))
        self.server_entry_1.set(server_values[0])
        self.server_entry_1.place(relx=0.3, rely=0.25, anchor='w')

        self.change_id_label_1 = customtkinter.CTkLabel(self.root, text="Change ID:", font=("Arial", 16))
        self.change_id_label_1.place(relx=0.15, rely=0.3, anchor='w')

        self.change_id_entry_1 = customtkinter.CTkEntry(self.root,  width = 340, font=("Arial", 14))
        self.change_id_entry_1.place(relx=0.3, rely=0.3, anchor='w')

        self.revision_id_label_1 = customtkinter.CTkLabel(self.root, text="Revision ID:", font=("Arial", 16))
        self.revision_id_label_1.place(relx=0.15, rely=0.35, anchor='w')

        self.revision_id_entry_1 = customtkinter.CTkEntry(self.root,  width = 340, font=("Arial", 14))
        self.revision_id_entry_1.place(relx=0.3, rely=0.35, anchor='w')

        self.separator_1 = ttk.Separator(self.root, orient='horizontal')
        self.separator_1.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.8)
        
        # Second repository info

        self.number_label_2 = customtkinter.CTkLabel(self.root, text="2", font=("Arial", 18))
        self.number_label_2.place(relx=0.05, rely=0.45, anchor='w')

        self.optional_label = customtkinter.CTkLabel(self.root, text="(optional)", font=("Arial", 12, "italic"))
        self.optional_label.place(relx=0.08, rely=0.45, anchor='w')

        self.server_label_2 = customtkinter.CTkLabel(self.root, text="Server:", font=("Arial", 16))
        self.server_label_2.place(relx=0.15, rely=0.5, anchor='w')

        self.server_entry_2 =  customtkinter.CTkComboBox(self.root, values=server_values,  width = 300, font=("Arial", 14))
        self.server_entry_2.set(server_values[0])
        self.server_entry_2.place(relx=0.3, rely=0.5, anchor='w')

        self.change_id_label_2 = customtkinter.CTkLabel(self.root, text="Change ID:", font=("Arial", 16))
        self.change_id_label_2.place(relx=0.15, rely=0.55, anchor='w')

        self.change_id_entry_2 = customtkinter.CTkEntry(self.root,width = 340, font=("Arial", 16))
        self.change_id_entry_2.place(relx=0.3, rely=0.55, anchor='w')

        self.revision_id_label_2 = customtkinter.CTkLabel(self.root, text="Revision ID:", font=("Arial", 16))
        self.revision_id_label_2.place(relx=0.15, rely=0.6, anchor='w')

        self.revision_id_entry_2 = customtkinter.CTkEntry(self.root,width = 340, font=("Arial", 14))
        self.revision_id_entry_2.place(relx=0.3, rely=0.6, anchor='w')

        self.separator_2 = ttk.Separator(self.root, orient='horizontal')
        self.separator_2.place(relx=0.5, rely=0.65, anchor='center', relwidth=0.8)

        # Third repository info

        self.number_label_3 = customtkinter.CTkLabel(self.root, text="3", font=("Arial", 18))
        self.number_label_3.place(relx=0.05, rely=0.7, anchor='w')

        self.optional_label = customtkinter.CTkLabel(self.root, text="(optional)", font=("Arial", 12, "italic"))
        self.optional_label.place(relx=0.08, rely=0.7, anchor='w')

        self.server_label_3 = customtkinter.CTkLabel(self.root, text="Server:", font=("Arial", 16))
        self.server_label_3.place(relx=0.15, rely=0.75, anchor='w')

        self.server_entry_3 =  customtkinter.CTkComboBox(self.root, values=server_values, width = 300, font=("Arial", 14))
        self.server_entry_3.set(server_values[0])
        self.server_entry_3.place(relx=0.3, rely=0.75, anchor='w')

        self.change_id_label_3 = customtkinter.CTkLabel(self.root, text="Change ID:", font=("Arial", 16))
        self.change_id_label_3.place(relx=0.15, rely=0.8, anchor='w')

        self.change_id_entry_3 = customtkinter.CTkEntry(self.root,width = 340, font=("Arial", 14))
        self.change_id_entry_3.place(relx=0.3, rely=0.8, anchor='w')

        self.revision_id_label_3 = customtkinter.CTkLabel(self.root, text="Revision ID:", font=("Arial", 16))
        self.revision_id_label_3.place(relx=0.15, rely=0.85, anchor='w')

        self.revision_id_entry_3 = customtkinter.CTkEntry(self.root,width = 340, font=("Arial", 14))
        self.revision_id_entry_3.place(relx=0.3, rely=0.85, anchor='w')

    def initialize_repositories(self, event=None):
        repository_1 = GerritRepository(self.server_entry_1.get(), self.change_id_entry_1.get(),self.revision_id_entry_1.get(), self.user)
        self.repositories = [repository_1]
        if self.change_id_entry_2.get() != "":
            repository_2 = GerritRepository(self.server_entry_2.get(), self.change_id_entry_2.get(),self.revision_id_entry_2.get(), self.user)
            self.repositories.append(repository_2)
        if self.change_id_entry_3.get() != "":    
            repository_3 = GerritRepository(self.server_entry_3.get(), self.change_id_entry_3.get(),self.revision_id_entry_3.get(), self.user)
            self.repositories.append(repository_3)
                
    def export(self):
        self.initialize_repositories()
        suites = []
        tests = []
        repos = []
        for repository in self.repositories:
            suites.append(repository.get_change_files())
            tests.append(repository.get_tests())
            repos.append(repository.get_repo())

        team_name = self.team_name_entry.get()
        sp_name = self.sp_name_entry.get()
        ms_word = MSWord(sp_name, team_name)
        ms_word.create_statistic_page(suites, tests)
        for repo, test in zip(repos, tests):
            ms_word.fill_test_data(repo, test)

        ms_word.save(sp_name)

        self.root.destroy()

    def start_import_window(self):
        self.repositories = self.run_gerrit_form_ui(self.user)
        

    def run_login(self):
        while True:
            self.login = Login(self.root)
            connection = self.login.get_login()

            if self.login.closed:
                break
          
            if connection:
                try:
                    connection.connect()
                    break
                except Exception as err:
                    self.show_exception(err)
                
        self.user = connection.user
        self.start_main_window(self.user)
        # self.root.deiconify()


    def on_close(self):
        self.root.destroy()
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

        

        