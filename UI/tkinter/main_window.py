import requests
import sys
from tkinter import messagebox, ttk
from customtkinter import *
from .login_window import LoginUI
from repository.repository_factory import RepositoryFactory
from json_handler import JSONHandler
from ..ui import UI

class TkinterUI(UI):
    def __init__(self, json_handler, repository_factory: RepositoryFactory):
        self.login = None
        self.gerrit_ui = None

        self.json_handler = json_handler
        self.repository_factory = repository_factory
        
        self.root = CTk()
        screen_height = self.root.winfo_screenheight()
        self.root.minsize(800,  int(screen_height * 0.8))
        self.root.title("Tolbot")
        self.root.resizable(width=False, height=False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        self.team_name = ""
        self.project_name = ""
        self.files = []
        self.tests = []
        self.repos = []
        
    def start_main_window(self, user):
        self.user = user
        self.welcome_label = CTkLabel(self.root, text=f"Hi, {self.user['username']}!", font=("Arial", 22))
        self.welcome_label.place(relx=0.05, rely=0.05, anchor='w')

        self.team_name_label = CTkLabel(self.root, text="Team name:", font=("Arial", 16))
        self.team_name_label.place(relx=0.3, rely=0.05, anchor='w')

        self.team_name_entry = CTkEntry(self.root, font=("Arial", 16))
        self.team_name_entry.place(relx=0.45, rely=0.05, anchor='w')

        self.project_name_label = CTkLabel(self.root, text="SP name:", font=("Arial", 16))
        self.project_name_label.place(relx=0.3, rely=0.1, anchor='w')

        self.project_name_entry = CTkEntry(self.root, font=("Arial", 16))
        self.project_name_entry.place(relx=0.45, rely=0.1, anchor='w')

        self.separator_1 = ttk.Separator(self.root, orient='horizontal')
        self.separator_1.place(relx=0.5, rely=0.15, anchor='center', relwidth=0.8)

        export_button = CTkButton(self.root, text="Export", command=self.export, font=("Arial", 22))
        export_button.place(relx=0.45, rely=0.95, anchor='center')

        self.create_gerrit_widgets()

        self.root.bind('<Return>', self.export)
        
        {"team_name": self.team_name, "project_name": self.project_name, "files": self.files, "repos": self.repos, "tests":self.tests}

    def create_gerrit_widgets(self):
        server_values = self.repository_factory.get_servers()

        self.change_id_entry = [None, None, None]
        self.revision_id_entry = [None, None, None]
        self.server_entry = [None, None, None]

        # First repository info

        self.number_label_1 = CTkLabel(self.root, text="1", font=("Arial", 18))
        self.number_label_1.place(relx=0.05, rely=0.2, anchor='w')

        self.server_label_1 = CTkLabel(self.root, text="Server:", font=("Arial", 16))
        self.server_label_1.place(relx=0.15, rely=0.25, anchor='w')

        self.server_entry[0] =  CTkComboBox(self.root, values=server_values, width = 300, font=("Arial", 14))
        if server_values:
            self.server_entry[0].set(server_values[0])
        self.server_entry[0].place(relx=0.3, rely=0.25, anchor='w')

        self.change_id_label_1 = CTkLabel(self.root, text="Change ID:", font=("Arial", 16))
        self.change_id_label_1.place(relx=0.15, rely=0.3, anchor='w')

        self.change_id_entry[0] = CTkEntry(self.root,  width = 340, font=("Arial", 14))
        self.change_id_entry[0].place(relx=0.3, rely=0.3, anchor='w')

        self.revision_id_label_1 = CTkLabel(self.root, text="Revision ID:", font=("Arial", 16))
        self.revision_id_label_1.place(relx=0.15, rely=0.35, anchor='w')

        self.revision_id_entry[0] = CTkEntry(self.root,  width = 340, font=("Arial", 14))
        self.revision_id_entry[0].place(relx=0.3, rely=0.35, anchor='w')

        self.separator_1 = ttk.Separator(self.root, orient='horizontal')
        self.separator_1.place(relx=0.5, rely=0.4, anchor='center', relwidth=0.8)
        
        # Second repository info

        self.number_label_2 = CTkLabel(self.root, text="2", font=("Arial", 18))
        self.number_label_2.place(relx=0.05, rely=0.45, anchor='w')

        self.server_label_2 = CTkLabel(self.root, text="Server:", font=("Arial", 16))
        self.server_label_2.place(relx=0.15, rely=0.5, anchor='w')

        self.server_entry[1] = CTkComboBox(self.root, values=server_values,  width = 300, font=("Arial", 14))
        if server_values:
            self.server_entry[1].set(server_values[0])
        self.server_entry[1].place(relx=0.3, rely=0.5, anchor='w')

        self.change_id_label_2 = CTkLabel(self.root, text="Change ID:", font=("Arial", 16))
        self.change_id_label_2.place(relx=0.15, rely=0.55, anchor='w')

        self.change_id_entry[1] = CTkEntry(self.root,width = 340, font=("Arial", 14))
        self.change_id_entry[1].place(relx=0.3, rely=0.55, anchor='w')

        self.revision_id_label_2 = CTkLabel(self.root, text="Revision ID:", font=("Arial", 16))
        self.revision_id_label_2.place(relx=0.15, rely=0.6, anchor='w')

        self.revision_id_entry[1] = CTkEntry(self.root,width = 340, font=("Arial", 14))
        self.revision_id_entry[1].place(relx=0.3, rely=0.6, anchor='w')

        self.separator_2 = ttk.Separator(self.root, orient='horizontal')
        self.separator_2.place(relx=0.5, rely=0.65, anchor='center', relwidth=0.8)

        # Third repository info

        self.number_label_3 = CTkLabel(self.root, text="3", font=("Arial", 18))
        self.number_label_3.place(relx=0.05, rely=0.7, anchor='w')

        self.server_label_3 = CTkLabel(self.root, text="Server:", font=("Arial", 16))
        self.server_label_3.place(relx=0.15, rely=0.75, anchor='w')

        self.server_entry[2] = CTkComboBox(self.root, values=server_values, width = 300, font=("Arial", 14))
        if server_values:
            self.server_entry[2].set(server_values[0])
        self.server_entry[2].place(relx=0.3, rely=0.75, anchor='w')

        self.change_id_label_3 = CTkLabel(self.root, text="Change ID:", font=("Arial", 16))
        self.change_id_label_3.place(relx=0.15, rely=0.8, anchor='w')

        self.change_id_entry[2] = CTkEntry(self.root,width = 340, font=("Arial", 14))
        self.change_id_entry[2].place(relx=0.3, rely=0.8, anchor='w')

        self.revision_id_label_3 = CTkLabel(self.root, text="Revision ID:", font=("Arial", 16))
        self.revision_id_label_3.place(relx=0.15, rely=0.85, anchor='w')

        self.revision_id_entry[2] = CTkEntry(self.root,width = 340, font=("Arial", 14))
        self.revision_id_entry[2].place(relx=0.3, rely=0.85, anchor='w')
                
    def export(self, event=None):
        repositories = [None, None, None]
        for i in range(3):   
            if self.change_id_entry[i].get() != "": 
                repositories[i] = self.repository_factory.create_repository(self.server_entry[i].get(), self.change_id_entry[i].get(),self.revision_id_entry[i].get(), self.user)

        for repository in repositories:
            if repository != None:
                self.files.append(repository.get_change_files())
                self.tests.append(repository.get_tests())
                self.repos.append(repository.get_repo())

        self.team_name = self.team_name_entry.get()
        self.project_name = self.project_name_entry.get()

        self.root.quit()

    def run(self):
        while True:
            self.login = LoginUI(self.root)
            connection = self.login.get_login()

            if self.login.closed:
                sys.exit()
          
            if connection:
                try:
                    connection.connect()
                    break
                except Exception as err:
                    self.notify_login_exception(err)
                
        self.user = connection.user
        self.start_main_window(self.user)
        self.root.mainloop()

        self.json_handler.export_to_json({
            "team_name": self.team_name,
            "project_name": self.project_name,
            "files": self.files,
            "repos": self.repos,
            "tests": self.tests
        })

    def on_close(self):
        self.root.destroy()
        sys.exit()
    
    def notify_login_exception(self,err):
        if isinstance(err, requests.exceptions.HTTPError):
            messagebox.showerror("LoginUI Failed", f"HTTP error occurred: {err}")
        elif isinstance(err, requests.exceptions.ConnectionError):
            messagebox.showerror("LoginUI Failed", f"Error connecting to Gerrit server: {err}")
        elif isinstance(err, requests.exceptions.Timeout):
            messagebox.showerror("LoginUI Failed", f"Request timed out: {err}")
        elif isinstance(err, requests.exceptions.RequestException):
            messagebox.showerror("LoginUI Failed", f"An error occurred: {err}")
        else:
            messagebox.showerror("LoginUI Failed", f"An unexpected error occurred: {err}")

    def notify(self, message):
        if isinstance(message, Exception):
            messagebox.showerror("Error",f"An error occured: {message}")
        else:
            messagebox.showinfo("Info", message)


        