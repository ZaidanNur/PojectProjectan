import os
import json
from datetime import datetime
from itertools import permutations

#Penampung data untuk diolah
nama_barang = []
berat = []
harga = []
kapasitas = int

#Elemen untuk menyimpan dan menload data
file_json = r'D:\@code\TUGAS\SMT 2\Tugas Akhir\record.json'
data_disimpan = []
tujuan = []
asal = str
nilai_maks_bantuan = int
barang_dipak = []
ongkir_minimal = int
jalur_min = []



def main():
    while True:
        ClearScreen()
        tittle()
        print(f"[1] Pengepakan dan Pengiriman Bantuan\n[2] Riwayat Kirim\n[3] Exit")
        try:
            user_input=int(input("Masukkan pilihan : "))
        except Exception:
            input("Format inputan salah mohon periksa kembali inputan anda ....")
            continue
        if user_input == 1:
            pengepakan_barang()
            input('Tekan enter untuk memasukkan tujuan...')
            lokasi_kirim()
            simpan_data(max_value=nilai_maks_bantuan,asalnya=asal[0],tujuannya=tujuan[0],nama_barang_dipak=barang_dipak,min_ongkir=ongkir_minimal,jalur_kirim=jalur_min)
            input('Tekan enter untuk kembali ke menu utama...')
            continue
        elif user_input == 2 :
            ClearScreen()
            tampilkan_data()
            input("Tekan enter untuk kembali ke menu awal...")
            continue
        elif user_input == 3 :
            print("========== TERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI ==========")
            exit()

def ReadJSON(data,tujuan): # Fungsi untuk membaca file json
    with open(data,'r') as file:  # Membuka file json
        reader = json.load(file) # Mengambil data dari file json
        for i in reader:
            tujuan.append(i) # Memasukkan data kedalam list penampung

def WriteJSON(data,asal):# Fungsi untuk menulis ulang file json
    with open(data,'w') as file: # Membuka file json
        json.dump(asal,file,indent=4) # Menulis ulang file json dengan data pada suatu list penampung

def tittle():
	print('='*50)
	print(f'{"BANTU.IN":^50}')
	print('='*50)

def ClearScreen(): # Fungsi untuk membersihkan command line
    os.system("cls" if os.name=="nt" else "clear")

# Digunakan untuk memasukkan data barang yang akan dipak oleh user secara manual
def pengepakan_barang():
	more_input = 'y'
	while more_input != 'n':
		ClearScreen()
		tittle()
		print('Masukkan data barang yang akan dipak')
		input_nama_barang = input(f"{'Masukkan nama barang':<30} : ")
		try:
			input_berat = int(input(f"{'Masukkan berat barang dalam Kg':<30} : "))
			input_harga = int(input(f"{'Masukkan harga barang dalam Rupiah':<30} : "))
		except Exception:
			print("Mohon periksa kembali inputan anda")
		check_data_input = input("Apakah inputan anda sudah benar ? (y/n)\n").lower()
		if check_data_input == 'y' :
			pass
		elif check_data_input == 'n':
			continue
		nama_barang.append(input_nama_barang)
		berat.append(input_berat)
		harga.append(input_harga)
		ClearScreen()
		tittle()
		more_input = input("Apakah ada inputan lagi ? (y/n)\n").lower()
	ClearScreen()
	tittle()
	kapasitas = int(input("Masukkan kapasitas wadah (Kg) : "))
	knapsack(berat,harga,kapasitas)

def knapsack(weight,price,capacity):
    global nilai_maks_bantuan
    global barang_dipak
    # nilai weight, price, dan capacity didapatkan dari inputan pada fungsi pengepakan_barang
    # yang ditampung dalam list berat, harga, dan kapasitas
    table = [[0 for col in range(capacity+1)] for row in range(len(weight)+1)]

    for row in range(len(weight)+1):
        for col in range(capacity+1):
            if row == 0 or col==0:
                table[row][col]=0
            elif weight[row-1] <= col:
                table[row][col] = max(table[row-1][col],table[row-1][col-weight[row-1]]+price[row-1])
            else:
                table[row][col] = table[row-1][col]
    ClearScreen()
    tittle()
    #value_maks merupakan nilai maksimal yang dihasilkan berdasarkan algoritma knapsack
    value_maks = table[len(weight)][capacity]
    nilai_maks_bantuan = value_maks
    print(f"{'Value maksimal yang didapatkan':<30} : Rp {value_maks:,}".replace(",","."))
    value_maks1 = value_maks
    capacity1=capacity
    #Kita mengecek barang apa saja yang bisa dipak lalu ditampung dalam list nama_barang_dipak
    things = []
    nama_barang_dipak = []
    #Memasukkan index barang yang dipak kedalam list things
    for x in range(len(weight),0,-1):
        if value_maks1 > 0 and (capacity1-weight[x-1]) > 0 :
            value_maks1 = value_maks1 - price[x-1]
            capacity1 -= (weight[x-1])
            things.append(x)
    num = 1
    print(f"{'Barang yang dipak'} : ")
	#Menampilkan nama barang yang ditampilkan dari list nama_barang berdasarkn index dalam list things
    for i in things:
        print(f"{num}. {nama_barang[i-1]}")
        num +=1
        nama_barang_dipak.append(nama_barang[i-1])
    barang_dipak = nama_barang_dipak
    print()
    # simpan_data(value_maks)

def node(graf,sp=0,nodes=[],count=0):
    if count==len(graf):
        k = permutations(nodes) # Mencari permutasi path yang mungkin
        all_nodes = []
        for i in k:
            all_nodes.append(i)
        return all_nodes
    elif count==sp:
        return node(graf,sp,nodes,count+1)
    else:
        nodes.append(count)
        return node(graf,sp,nodes,count+1)

def TSP(graf,sp,daerah,nodes=[],c_cost=0,count=0,all_cost=[]):
    global ongkir_minimal
    global jalur_min
    if count == len(nodes):
        min_cost = min(all_cost)
        ongkir_minimal = min_cost
        location = [i for i, val in enumerate(all_cost) if val==min_cost]
        print("Rute dengan ongkos minimal :")
        for i in location:
            path_min_cost = [daerah[0]]
            # print(daerah[0],end=' -> ')
            for j in nodes[i]:
                # print(daerah[j],end=' -> ')
                path_min_cost.append(daerah[j])
            # print(daerah[0])
            path_min_cost.append(daerah[0])
            jalur_min.append(path_min_cost)
            print(' -> '.join(path_min_cost))
        print(f"Ongkos minimal : Rp {int(min_cost):,}".replace(',','.'))
        return min_cost
    else:
        nodes_now= nodes[count]
        k = sp
        for j in nodes_now:
            c_cost+=graf[k][j]
            k=j
        c_cost+=graf[k][sp]
        all_cost.append(c_cost)
        return TSP(graf,sp,daerah,nodes,0,count=count+1,all_cost=all_cost)
        # TSP(graf_tsp,0,tujuan_bantuan,node(graf_tsp,0,[],0))

def lokasi_kirim():
    global asal
    ClearScreen()
    tittle()
    tujuan_bantuan = input("Masukkan lokasi tujuan bantuan\nex : Papua, Maluku, Kalimantan\n-> ").lower().replace(' ','').split(',')
    Kota_asal_bantuan = input(f"Masukkan asal bantuan dikirim : ").lower()

    if Kota_asal_bantuan in tujuan_bantuan:
        pass
    else:
        tujuan_bantuan.insert(0,Kota_asal_bantuan)
    
    if len(tujuan_bantuan) > 2:
        pass
    else:
        lokasi_kirim()
    tujuan.append(tujuan_bantuan[1:])
    asal = tujuan_bantuan[:1]
    ClearScreen()
    tittle()
    graf_tsp = []
    for i in range(len(tujuan_bantuan)):
        temp_graf = []
        for j in range(len(tujuan_bantuan)):
            if i == j:
                input_jarak = 0
            else:
                hayo = f"Jarak {tujuan_bantuan[i]} dengan {tujuan_bantuan[j]} (Km)"
                input_jarak = int(input(f"{hayo:<32} : "))
                # angka 5 adalah rata2 Km yang bisa ditempuh mobil box pengiriman dan 9400 adalah harga solar non-subsis saat ini
                input_jarak = (input_jarak/5)*9400
            temp_graf.append(input_jarak)
        graf_tsp.append(temp_graf)
    ClearScreen()
    tittle()
    TSP(graf_tsp,0,tujuan_bantuan,node(graf_tsp,0,[],0))

def simpan_data(max_value,asalnya,tujuannya,nama_barang_dipak,min_ongkir,jalur_kirim):
    global data_disimpan
    global tujuan
    global asal
    global nilai_maks_bantuan 
    global barang_dipak
    global ongkir_minimal
    global jalur_min
    ReadJSON(file_json,data_disimpan)
    tanggal = datetime.now()
    tanggal_hari_ini = f"{tanggal.strftime('%d')} {tanggal.strftime('%B')} {tanggal.strftime('%Y')}"
    data_pengepakan_barang = dict()
    try:
        data_pengepakan_barang["no"] = data_disimpan[-1]["no"]+1
    except Exception:
        data_pengepakan_barang["no"] = 1
    data_pengepakan_barang["tanggal"] = tanggal_hari_ini
    data_pengepakan_barang["asal"]= asalnya
    data_pengepakan_barang["tujuan"] = tujuannya
    data_pengepakan_barang["maks value"] = max_value
    data_pengepakan_barang["barang dipak"] = nama_barang_dipak
    data_pengepakan_barang["ongkos minimal"] = min_ongkir
    data_pengepakan_barang["jalur termurah"] = jalur_kirim
    data_disimpan.append(data_pengepakan_barang)
    WriteJSON(file_json,data_disimpan)
    data_disimpan = []
    tujuan = []
    asal = str
    nilai_maks_bantuan = int
    barang_dipak = []
    ongkir_minimal = int
    jalur_min = []

def tampilkan_data():
    ReadJSON(file_json,data_disimpan) # membaca file json
    # variabel untuk numbering otomatis
    print('='*130) # batas
    Header = list() # list untuk menampung header
    head = data_disimpan[0].keys() # menggambil key dari dictionary dalam list data_disimpan untuk header
    for i in head:
        Header.append(i) # menambahkan isi variabel head ke list Header
    # mencetak header
    print(f"{Header[0]:<4}{Header[1]:<18}{Header[2]:<18}{Header[3]:<18}".upper().rstrip())
    print('='*130)
    for isi in data_disimpan:
        a = ", ".join(isi['tujuan'])
        print(f"{isi['no']:<4}{isi['tanggal']:<18}{isi['asal']:<18}{a:<18}".rstrip())
        print()# memberi enter
    pilih_bang = int(input("Pilih nomor untuk melihat detail : "))
    ClearScreen()
    tittle()
    data_detail = dict
    for i in data_disimpan:
        if pilih_bang == i["no"]:
            data_detail = i
    print(f"{'Tanggal pengiriman':<30} : ",data_detail['tanggal'])
    print(f"{'Asal pengiriman':<30} : ",data_detail['asal'])
    print(f"{'Tujuan pengiriman':<30} : ",", ".join(data_detail['tujuan']))
    uang = f"{isi['maks value']:,}".replace(",",".")
    print(f"{'Besar bantuan':<30} : ",uang)
    print(f"{'Bantuan berupa':<30} : ",", ".join(data_detail['barang dipak']))
    ongkir = f"{int(data_detail['ongkos minimal']):,}".replace(",",".")
    print(f"{'Ongkos pengiriman':<30} : ",ongkir)
    print(f"{'Jalur pengiriman dengan cost minimal':<30} : ")
    for i in data_detail['jalur termurah']:
        print(" -> ".join(i))
   
    data_disimpan.clear() # membersihkan variabel data_disimpan



# TSP(Graf_soal,0,hiyaa,node(Graf_soal,0,[],0))

# tampilkan_data()
# lokasi_kirim()
# TSP(Graf_soal,0,node(Graf_soal,0,[],0))
if __name__ == '__main__':
	main()
# pengepakan_barang()