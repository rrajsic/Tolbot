from Export.MSWord import MSWord
from UI.ui import UI
from User.User import User



def main():
    ui = UI()
    ui.run_login()
    ui.root.mainloop()

if __name__ == "__main__":
    main()