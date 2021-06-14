import json #Mengimport module json
from datetime import datetime as dt #Mengimport library datetime lalu memanggil module datetime sebagai dt
import os #Mengimport module os

fileJSON = 'E:\code\python\.venv\TUGAS\databuku.json' # Path file databuku.json
filePeminjam = "E:\code\python\.venv\TUGAS\datapeminjam.json" # Path file datapeminjam.json
DataKita = []  # list kosong untuk menampung data yang akan diolah
Login = False # Status login, saat berhasil login akan bernilai True
status = '' # Status akun yang digunakan login

def ReadJSON(data=fileJSON,tujuan=DataKita): # Fungsi untuk membaca file json
    with open(data,'r') as file:  # Membuka file json
        reader = json.load(file) # Mengambil data dari file json
        for i in reader:
            tujuan.append(i) # Memasukkan data kedalam list penampung

def WriteJSON(data=fileJSON,asal=DataKita):# Fungsi untuk menulis ulang file json
    with open(data,'w') as file: # Membuka file json
        json.dump(asal,file,indent=4) # Menulis ulang file json dengan data pada suatu list penampung

def tittle():
    print('''
,--.     ,      .                       
|        |    o |                       
|-   --- |    . |-. ;-. ,-: ;-. ;-. . . 
|        |    | | | |   | | |   |   | | 
`--'     `--' ' `-' '   `-` '   '   `-| 
                                    `-'
    ''')

def ClearScreen(): # Fungsi untuk membersihkan command line
    os.system("cls" if os.name=="nt" else "clear")

def TambahUser(): # Fungsi untuk menambahkan anggota perpustakaan
    DataUserLogin = [] # Variabel list penampung
    ReadJSON('E:\code\python\.venv\TUGAS\login.json',DataUserLogin) # Membaca file json login.json

    NewUser = dict() # Membuat dictionary baru dengan nama NewUser
    NewUser['username'] = input("Masukkan NIM : ") # menambahkan key 'username' dan value nya
    NewUser['password'] = input("Masukkan password :") # menambahkan key 'password' dan value nya
    NewUser['status'] = 'user' # menambahkan key 'status' dan value nya

    DataUserLogin.append(NewUser) # menambahkan dictionary NewUser kedalam list DataUserLogin

    WriteJSON('E:\code\python\.venv\TUGAS\login.json',DataUserLogin) # menulis file login.json dengan data pada DataUserLogin

def User_login(): # fungsi untuk melakukan login
    DataUserLogin = [] # list penampung data
    ReadJSON('E:\code\python\.venv\TUGAS\login.json',DataUserLogin) # Membaca file login.json dan memasukkannya ke list DataUserLogin
    global Login # Mengambil nilai variabel Login
    global status # Mengambil nilai variabel status
    print("HALAMAN LOGIN")
    while Login != True: # Perulangan untuk mengecek user login
        input_username = input("Masukkan username : ") # user diminta memasukkan username
        for i in DataUserLogin: # looping untuk pengecekan data
            if i['username'] == input_username: # percabangan jika username yang dimasukkan ada
                while Login != True:
                    input_pw = input("Masukkan password : ") # user diminta memasukkan password
                    if input_pw == i['password']: #percabangan saat username dan password telah sesuai
                        print("Anda berhasil login")
                        status = i['status'] # mengganti variabel status dengan value key 'status'
                        Login = True # mengganti nilai variabel Login
                    else:
                        print("Password anda salah ! mohon periksa kembali ") # percabangan saat password salah
        if Login == False: # percabangan apabila username tidak ada di database
            print('Username yang anda masukkan tidak tersedia.')

def AddBooktoList():
    DataKita.clear() # membersihkan isi list DataKita
    ReadJSON() # membaca file databuku,json
    panjang_awal = len(DataKita) # Melihat panjang data dalam variabel DataKita

    NewBook = dict() # membuat dictionary baru bernama NewBook
    NewBook['nama buku'] = input("Masukkan nama buku : ") # membuat key 'nama buku' dengan value inputan dari user
    NewBook['tahun terbit'] = input("Masukkan tahun terbit : ") # membuat key 'tahun terbit' dengan value inputan dari user
    NewBook['penerbit'] = input('Masukkan penerbit : ')# membuat key 'penerbit' dengan value inputan dari user
    NewBook['kode buku'] = [] # membuat key 'kode buku' dengan value sebuah list kosong
    InputKode = input('Masukkan kode buku : ') # meminta user untuk menginputkan kode buku baru
    NewBook['kode buku'].append(InputKode) # menambahkan kode buku inputan ke list kosong
    NewBook['buku dipinjam'] = [] #membuat key 'buku dipinjam' dengan value list kosong

    DataKita.append(NewBook) # menambahkan dictionari NewBook ke list DataKita

    WriteJSON() # menulis ulang file databuku.json
    panjang_baru = len(DataKita) # melihat panjang data dalam variabel DataKita
    if panjang_baru > panjang_awal: # pengecekan panjang datanya bertambah atau tidak
        print("[+] Data buku berhasil di masukkan !!")
    DataKita.clear() # membersihkan isi list DataKita

def ShowBookonList():
    ReadJSON() # membaca file json
    numbering = 1 # variabel untuk penomoran otomatis

    print('='*130) # batas
    Header = list() # list Header untuk menyimpan header
    head = DataKita[0].keys() # menggambil key dari dictionary dalam list DataKita untuk header
    for i in head:
        Header.append(i) # menambahkan isi variabel head ke list Header
    print(f"{'No':<4}{Header[0]:<46}{Header[1]:<18}{Header[2]:<44}{'jumlah':^10}".upper().rstrip()) # mem- print header
    print('='*130) # batas
    for isi in DataKita:
        JumlahBuku = len(isi['kode buku']) # menghitung jumlah buku berdasarkan kodenya
        # menuliskan isi dari variabel DataKita
        print(f"{str(numbering):<4}{isi['nama buku']:<46}{isi['tahun terbit']:<18}{isi['penerbit']:<44}{JumlahBuku:^10}".rstrip())
        numbering+=1 # menambahkan penomoran otomatis
        print() # memberikan enter
    DataKita.clear() # membersihkan variabel DataKita
  
def AddSameBook(): # fungsi untuk menambahkan buku yang sama tapi kode buku berbeda
    ReadJSON() # membaca file databuku.json
    TambahBuku = int(input("Masukkan nomor buku yang ditambahkan : ")) # meminta user memasukkan no buku yang ditambahkan berdasarkan list yang diberikan
    IdentitaBuku = [] # list kosong untuk menampung data buku
    for data in DataKita: # pengecekan 
        if DataKita.index(data) == (TambahBuku-1): # mencari index yang sesuai dengan inputan
            IdentitaBuku.append(data) # mengambil data buku yang diinginkan
            DataKita.pop(DataKita.index(data)) # menghapus data dari list penampung DataKita

    for isi in IdentitaBuku: # pengecekan pada isi variabel IdentitasBuku
        kodebuku = isi['kode buku'] # menapung value dari key 'kode buku'
        OlahKode = isi['kode buku'][-1].split('-') # mengakses kode terakhir lalu memisahkan jadi 2 bagian
        Last3Kode = (OlahKode[0][:3] +'00' + str(int(OlahKode[0][3:]) +1)) # membuat kode nomor baru
        OlahKode[0] = Last3Kode # mengganti kode nomor
        NewKode = '-'.join(OlahKode) # menggabungkan kembali kode yang terpisah tadi
        kodebuku.append(NewKode) # menambahkan kode baru yang dihasilkan 
        for i in IdentitaBuku:
            DataKita.insert((TambahBuku-1),i) # memasukkan kembali data buku ke list DataKita
    WriteJSON() # menulis ulang file databuku.json
    DataKita.clear() # membersihkan variabel DataKita

def deletBukuOnList(): # fungsi untuk menghapus kode buku yang ada 
    ReadJSON() # membaca file databuku.json
    input_KodeBuku_dihapus = input("Masukkan kode buku yang ingin dihapus : ") # user diminta memasukkan kode buku yang akan dihapus
    for i in DataKita:
        for j in i['kode buku']:
            if j == input_KodeBuku_dihapus and j not in i['buku dipinjam']: # mencari kode yang diinput user
                i['kode buku'].pop(i['kode buku'].index(j)) # kode buku dihapus
                if len(i['kode buku']) == 0: # pengecekan apakah ada kode buku lain dalam data yang sama
                    DataKita.pop(DataKita.index(i)) # jika tidak, data buku akan dihapus
    WriteJSON() # menulis ulang file databuku.json
    DataKita.clear() # membersihkan list Datakita

def tanggalKembali(Temp): # fungsi untuk membuat tanggal kembali buku yang dipinjam
    if (int(Temp[0]) + 7) > 30 and (int(Temp[1]) == 4 or int(Temp[1]) == 6 or int(Temp[1]) == 9 or int(Temp[1]) == 11) :
        Temp[0] = str((int(Temp[0]) + 7) - 30)
        Temp[1] = str(int(Temp[1])+1)
    elif (int(Temp[0]) + 7) > 31 and (int(Temp[1]) == 1 or int(Temp[1]) == 3 or int(Temp[1]) == 5 or int(Temp[1]) == 7 or int(Temp[1]) == 8 or int(Temp[1]) == 10 or int(Temp[1]) == 12 ):
        Temp[0] = str((int(Temp[0]) + 7) - 31)
        if int(Temp[1]) == 12:
            Temp[1]= '1'
        else:
            Temp[1] = str(int(Temp[1])+1)
    elif (int(Temp[0]) + 7) > 28 and int(Temp[1]) == 2:
        if int(Temp[2]) % 4 == 0:
            Temp[0] = str((int(Temp[0]) + 7) - 29)
            Temp[1] = str(int(Temp[1])+1)
        else:
            Temp[0] = str((int(Temp[0]) + 7) - 28)
            Temp[1] = str(int(Temp[1])+1)
    else:
        Temp[0] = str(int(Temp[0]) + 7)
    NewDate = '-'.join(Temp)
    return NewDate

def PinjamBuku(): # fungsi untuk mencatat buku yang dipinjam
    Peminjam = [] # list penampung data
    ReadJSON(filePeminjam,Peminjam) # membaca data dalam file datapeminjam.json
    inputNIM = input('Masukkan NIM : ') # meminta user untuk memasukkan NIM
    ada = True # variabel yang digunakan untuk pengecekan NIM
    if ada==True:
        for i in Peminjam:
            if inputNIM == i['NIM']: # mencari NIM yang sama dengan inputan
                KodeBuku = input("Masukkan kode buku : ") # meminta inputan kode buku dari user
                cariDataBuku(KodeBuku,i['data buku']) # fungsi untuk mencari data buku berdasarkan kode buku
                ada = False
    if ada == True: # percabangan dijalankan jika NIM yang dimasukkan tidak ada di database
        DataPeminjam = dict()
        DataPeminjam['NIM'] = inputNIM
        DataPeminjam['nama mahasiswa'] = input('Masukkan nama mahasiswa : ') # user diminta untuk menginputkan nama mahasiswa
        DataPeminjam['data buku'] = [] # membuat key 'data buku' dengan value list kosong untuk menampung data buku
        KodeBuku = input("Masukkan kode buku : ") # meminta inputan kode buku dari user
        cariDataBuku(KodeBuku,DataPeminjam['data buku']) # fungsi untuk mencari data buku berdasarkan kode buku
        Peminjam.append(DataPeminjam)# menambahkan dictionary DataPeminjam 
    WriteJSON(filePeminjam,Peminjam) # menulis ulang file datapeminjam.json denga data dari variabel Peminjam
    recordTerpinjam(KodeBuku) # fungsi untuk memasukkan kode buku dipinjam

def cariDataBuku(inputan,tujuan): # fungsi untuk mencari data buku berdasarkan kode buku
    ReadJSON() # membaca file databuku.json
    for data in DataKita:
        for dat in data['kode buku']:
            if inputan == dat: # mencari data yang sesuai dengan inputan
                data['kode buku'] = inputan
                data['tanggal pinjam'] = dt.now().strftime("%d-%m-%Y") # membuat tanggal saat meminjam buku yaitu hari ini
                Temp = data['tanggal pinjam'].split('-') # memisahkan tanggal menjadi sebuah list
                data['tanggal kembali'] = tanggalKembali(Temp) # membuat tanggal baru yaitu 7 hari setelah peminjaman
                data.pop('buku dipinjam') # menghapuskan key 'buku dipinjam' 
                tujuan.append(data) # menambahkan data dari buku dengan kode buku yang dicari
    DataKita.clear() # membersihkan variabel DataKita

def recordTerpinjam(inputan): # fungsi untuk menambahkan kode buku dipinjam dalam list buku dipinjam
    ReadJSON() # membaca file databuku.json
    for data in DataKita:
        for dat in data['kode buku']:
            if inputan == dat:
                data['buku dipinjam'].append(inputan)
    WriteJSON() # menulis ulang file databuku.json

def ShowBookPeminjam(): # fungsi untuk menampilkan list buku yang tersedia
    ReadJSON() # membaca file json
    numbering = 1 # variabel untuk numbering otomatis

    print('='*130) # batas
    Header = list() # list untuk menampung header
    head = DataKita[0].keys() # menggambil key dari dictionary dalam list DataKita untuk header
    for i in head:
        Header.append(i) # menambahkan isi variabel head ke list Header
    # mencetak header
    print(f"{'No':<4}{Header[0]:<46}{Header[1]:<18}{Header[2]:<44}{'buku tersedia':^15}".upper().rstrip())
    print('='*130)
    for isi in DataKita:
        JumlahBuku = (len(isi['kode buku']) - len(isi['buku dipinjam'])) # menghitung jumlah buku yang belum dipinjam
        # nebcetak isi dalam file databuku.json
        print(f"{str(numbering):<4}{isi['nama buku']:<46}{isi['tahun terbit']:<18}{isi['penerbit']:<44}{JumlahBuku:^15}".rstrip())
        numbering+=1 # penambahan pada autonumbering
        print()# memberi enter
    DataKita.clear() # membersihkan variabel DataKita

def ListPeminjam(): # melihat siapa saja yang meminjam buku
    DaftarPeminjam = [] # list penampung data
    ReadJSON(data="E:\code\python\.venv\TUGAS\datapeminjam.json",tujuan=DaftarPeminjam) # membaca isi file datapeminjam.json
    print("="*100) # batas
    No = 1 # penomoran otomatis
    print(f"{'no':<10}{'NIM':<20}{'Nama':<40}".upper().rstrip()) # menampilkan header
    print("="*100) # batas
    for isi in DaftarPeminjam:
        print(f"{No:<10}{isi['NIM']:<20}{isi['nama mahasiswa']:<40}") # menampilkan data dalam variabel DaftarPeminjam
        No += 1 # menambahkan 1 pada penomoran
        print() # memberi enter

def cekBukuDipinjam(): # melihat buku apa saja yang di pinjam oleh seseorang
    ListPeminjam() # memanggil fungsi ListPeminjam
    DaftarPeminjam = [] # list penampung data
    ReadJSON(data="E:\code\python\.venv\TUGAS\datapeminjam.json",tujuan=DaftarPeminjam) # membaca isi file datapeminjam.json
    Pilih = int(input("Masukkan nomor yang ingin di cek : ")) # user diminta menginputkan nomor urut nama yang ingin dicek
    buku_dipinjam = [] # list untuk menampung data buku yang dipinjam
    will_show = [] # list menampung data peminjam
    for i in DaftarPeminjam:
        if DaftarPeminjam.index(i) == (Pilih-1):
            will_show = i # mengambil data yang diinginkan
            for buku in i['data buku']:
                buku_dipinjam.append(buku) # memasukkan data buku yang dipinjam
    ClearScreen() # fungsi untuk membersihkan layar command line
    print(f"Nama mahasiswa : {will_show['nama mahasiswa']}") # mencetak nama peminjam
    print(f"NIM            : {will_show['NIM']}") # mencetak NIM peminjam
    print()
    numbering = 1 # variabel untuk penomoran
    print('='*112) # garis batas
    Header = list() # list untuk menampung header
    try:
        head = buku_dipinjam[0].keys() # menggambil key dari dictionary dalam list buku_dipinjam untuk header
        for i in head:
            Header.append(i) # menambahkan isi variabel head ke list Header
        print(f"{'No':<4}{Header[0]:<50}{Header[4]:<18}{Header[5]:<30}{'kode buku':^10}".upper().rstrip()) # untuk menampilkan header
        print('='*112) # garis batas
        for isi in buku_dipinjam:
            # untuk menampilkan data yang ada pada variabel buku_dipinjam
            print(f"{str(numbering):<4}{isi['nama buku']:<50}{isi['tanggal pinjam']:<18}{isi['tanggal kembali']:<30}{isi['kode buku']:^10}".rstrip())
            numbering+=1 # menambahkan 1 pada penomoran
            print() # memberi enter
    except: # pengecekan error
        print("Tidak ada buku yang dipinjam.")
    
def KembalikanBuku(): # fungsi untuk mengembalikan buku
    BukuKembali = [] # list penampung data
    ReadJSON(filePeminjam,BukuKembali) # membaca file datapeminjam.json
    Input_Kembali = input("Masukkan kode buku yang dikembalikan : ") # meminta inputan kode buku yang dikembalikan
    for i in BukuKembali: # melihat isi variabel BukuKembali
        for j in i['data buku']: # melihat value dari key 'data buku' tiap item pada variabel BukuKembali
            if j['kode buku'] == Input_Kembali: # mencari kode buku yang sama dengan inputan
                i['data buku'].pop(i['data buku'].index(j)) # menghapus data buku dengan kode buku yang sesuai
    WriteJSON(filePeminjam,BukuKembali) # menulis ulang file datapeminjam.json
    DelrecordTerpinjam(Input_Kembali) # menghapus kode buku  dari list buku dipinjam

def DelrecordTerpinjam(inputan): # fungsi untuk menghapus record buku yang telah dikembalikan
    DataKita.clear()
    ReadJSON()
    for data in DataKita:
        for dat in data['buku dipinjam']:
            if inputan == dat:
                data['buku dipinjam'].pop(data['buku dipinjam'].index(dat))
    WriteJSON()
    DataKita.clear()

def menuPustakawan(): # fungsi untuk looping menu pustakawan
    while True:
        ClearScreen()
        tittle()
        print("[1] Tampilkan Daftar Buku\n[2] Tambahkan buku\n[3] Hapus buku\n[4] Lihat buku dipinjam\n[5] Tambah anggota\n[6] Exit".rstrip())
        try:
            InputUser=int(input("Masukkan pilihan anda : "))
        except:
            print("[-]Inputan anda tidak tersedia mohon inputkan ulang")
            input("Tekan enter untuk lanjut ...")
            continue
        if InputUser == 1 :
            ClearScreen()
            ShowBookonList()
            input("Tekan enter untuk kembali ...")
        elif InputUser == 2:
            ClearScreen()
            ShowBookonList()
            print('[1] Tambahkan buku baru\n[2] Tambahkan buku yang sama')
            PilihTambah = int(input("Masukkan mode yang diinginkan : "))
            if PilihTambah == 1:
                AddBooktoList()
                input("Tekan enter untuk kembali ...")
            elif PilihTambah == 2:
                AddSameBook()
                input("Tekan enter untuk kembali ...")
        elif InputUser == 3:
            ClearScreen()
            deletBukuOnList()
            print("[+] Buku telah behasil dihapus !!")
            input("Tekan enter untuk kembali ...")
        elif InputUser == 4 :
            ClearScreen()
            try :
                cekBukuDipinjam()
            except:
                print("Input yang anda masukkan salah !!")
                continue
            input("Tekan enter untuk lanjut ...")
        elif InputUser == 5 :
            TambahUser()
            print("[+] Daftar anggota berhasil diperbaharui ")
            input("Tekan enter untuk lanjut ...")
        elif InputUser == 6:
            ClearScreen()
            print("Terimakasih telah menggunakan program ini !! ")
            exit()

def menuPeminjam(): # fungsi untuk looping menu peminjam
     while True:
        ClearScreen()
        tittle()
        print(
            "[1] Tampilkan Daftar Buku\n[2] Pinjam buku\n[3] Kembalikan buku\n[4] Lihat buku dipinjam\n[5] Exit".rstrip())
        try:
            InputUser=int(input("Masukkan pilihan anda : "))
        except:
            print("[-]Inputan anda tidak tersedia mohon inputkan ulang")
            input("Tekan enter untuk lanjut ...")
            continue
        if InputUser == 1 :
            ClearScreen()
            ShowBookPeminjam()
            input("Tekan enter untuk lanjut ...")
        elif InputUser == 2 :
            ClearScreen()
            PinjamBuku()
            print("[+] Data peminjaman buku telah terekam !!")
            input("Tekan enter untuk lanjut ...")
        elif InputUser == 3:
            ClearScreen()
            KembalikanBuku()
            print("[+] Data peminjaman buku telah diperbarui !!")
            input("Tekan enter untuk lanjut ...")
        elif InputUser == 4 :
            ClearScreen()
            try :
                cekBukuDipinjam()
            except:
                print("Inputan yang anda masukkan salah !!")
                continue
            input("Tekan enter untuk lanjut ...")
        elif InputUser == 5:
            ClearScreen()
            print("Terimakasih telah menggunakan program ini !! ")
            exit()

def mainloop():
    tittle()
    User_login()
    input("Enter untuk lanjut ....")
    if status == 'admin':
        menuPustakawan()
    if status == 'user':
        menuPeminjam()
        
mainloop()


