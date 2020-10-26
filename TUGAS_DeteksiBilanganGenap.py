print("================================================")
print("\t   Program Deteksi Ganjil/Genap")
print("================================================")

for i in range(5):
    inputAngka = input("\nMasukkan Bilangan  :  ")
    try:
        if (float(inputAngka) % 2) == 0 :
            print("Bilangan yang anda masukkan bilangan genap")
            print("================================================")
        elif (float(inputAngka) % 2) == 1 :
            print("Bilangan yang anda masukkan bilangan ganjil")
            print("================================================")
        else :
            print("Bilangan yang anda masukkan bilangan desimal")
            print("================================================")

    except:
        print(f"Broo ..{inputAngka} Bukan Bilangan")
        print("============================================")
   
