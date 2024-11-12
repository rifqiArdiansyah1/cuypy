import main
def start():
    while True:
        print("ini adalah Warung Mini APPS!")
        user_option = input("Kembali ke menu utama? [y/n]")
        if user_option == "y":
            main.menu()
            break

if __name__ == "__main__":
    start()