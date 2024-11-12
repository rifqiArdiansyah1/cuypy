from libs import welcome_message, exit_program
from games import cuypy
from tools import warung

def menu():
    user_option = int(input("Menu program:\n 1. CUYPY Games\n 2. Warung Mini\n 3. Keluar Program\n\nSilahkan Pilih:"))
    if user_option == 1:
        cuypy.start()
    elif user_option == 2:
        warung.start()
    elif user_option == 3:
        exit_program()
    else:
        print("Hanya boleh memilih menu yang tersedia!")

def main():
    welcome_message()
    menu()

if __name__ == '__main__':
    main()