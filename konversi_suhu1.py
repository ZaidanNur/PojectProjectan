import os
def main():
    print("\t\tKONVERSI SUHU\t")
    print("Pilih Satuan Suhu Yang Akan Dikonversikan\n")
    print("1.Celcius","\n2.Fahrenheit","\n3.Kelvin","\n4.Reamur")

def back_main():
    inp_ganti = str(input("Pilih Satuan Lain ? (y/n)"))
    if inp_ganti == "y" :
        main()
        inp_pilihan = int(input("Masukkan Nomer Satuan Yang Dipilih\n(1/2/3/4) :"))
    if inp_ganti== "n":
        pass
def Celsius():
    inp_celcius = float(input("Masukkan Suhu Dalam Celcius :"))
    cel_to_far = (inp_celcius * (9/5)) + 32
    cel_to_kel = inp_celcius + 273
    cel_to_re = (4/5)* inp_celcius
    print(inp_celcius)
    print("Fahrenheit :",cel_to_far)
    print("Kelvin     :",cel_to_kel)
    print("Reamur     :",cel_to_re)
def Fahrenheit():
    inp_far = float(input("Masukkan Suhu Dalam Fahrenheit :"))
    far_to_cel = (inp_far - 32)*(5/9)
    far_to_kel = far_to_cel + 273
    far_to_re = (4/5)* far_to_cel
    print("Celcius    :",far_to_cel)
    print("Kelvin     :",far_to_kel)
    print("Reamur     :",far_to_re)
def Kelvin():
    inp_kel = float(input("Masukkan Suhu Dalam Kelvin :"))
    kel_to_cel = inp_kel- 273
    kel_to_far = (kel_to_cel * (9/5)) + 32
    kel_to_re = (4/5)* kel_to_cel
    print("Celcius    :",kel_to_cel)
    print("Fahreheit  :",kel_to_far)
    print("Reamur     :",kel_to_re)
def Reamur():
    inp_re = float(input("Masukkan Suhu Dalam Reamur :"))
    re_to_cel = (5/4)* inp_re
    re_to_far= (re_to_cel * (9/5)) + 32
    re_to_kel = re_to_cel + 273
    print("Celcius    :",re_to_cel)
    print("Fahrenhei  :",re_to_far)
    print("Kelvin     :",re_to_kel)


main()
inp_pilihan = int(input("Masukkan Nomer Satuan Yang Dipilih\n(1/2/3/4) :"))
#os.system("clear")
while inp_pilihan == 1 :
    Celsius()
    inp_ganti = str(input("Pilih Satuan Lain ? (y/n)"))
    if inp_ganti == "y" :
        main()
        inp_pilihan = int(input("Masukkan Nomer Satuan Yang Dipilih\n(1/2/3/4) :"))
    if inp_ganti== "n":
        pass
while inp_pilihan == 2 :
    Fahrenheit()
    inp_ganti = str(input("Pilih Satuan Lain ? (y/n)"))
    if inp_ganti == "y" :
        main()
        inp_pilihan = int(input("Masukkan Nomer Satuan Yang Dipilih\n(1/2/3/4) :"))
    if inp_ganti== "n":
        pass
while inp_pilihan == 3 :
    Kelvin()
    inp_ganti = str(input("Pilih Satuan Lain ? (y/n)"))
    if inp_ganti == "y" :
        main()
        inp_pilihan = int(input("Masukkan Nomer Satuan Yang Dipilih\n(1/2/3/4) :"))
    if inp_ganti== "n":
        pass
while inp_pilihan == 4 :
    Reamur()
    inp_ganti = str(input("Pilih Satuan Lain ? (y/n)"))
    if inp_ganti == "y" :
        main()
        inp_pilihan = int(input("Masukkan Nomer Satuan Yang Dipilih\n(1/2/3/4) :"))
    if inp_ganti== "n":
        pass
