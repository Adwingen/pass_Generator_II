# main.py
from ui_setup import UI_Setup
from commands import PasswordManager

def main():
    password_manager = PasswordManager()
    ui = UI_Setup(password_manager)
    ui.window.mainloop()

if __name__ == '__main__':
    main()








