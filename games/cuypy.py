import random
import main
def start():
    while True:
        bentuk_goa = "|_|"
        goa = [bentuk_goa] * 4
        
        cuypy_position = int(random.randint(1, 4))
        
        goa_cuypy = goa.copy()
        goa_cuypy[cuypy_position - 1] = "CUYPY"
        goa = ' '.join(goa)
        goa_cuypy = ' '.join(goa_cuypy)
        
        print(goa)
        pilihan_user = int(input("Menurut kamu cuypy berada di goa no berapa? [1/2/3/4]:"))

        if pilihan_user == cuypy_position :
            print("Selamat kamu menang!")
        else :
            print("Kamu kalah, coba lagi")

        print(f"CUYPY berada di goa nomor {cuypy_position} \n {goa_cuypy}")
        
        main_ulang = input("apakah kamu ingin bermain lagi? [y/n]:")
        
        if main_ulang == "y":
            continue
        elif main_ulang == "n":
            main.menu()
            break
        else:
            main.menu()
            break

if __name__ == "__main__":
    start()