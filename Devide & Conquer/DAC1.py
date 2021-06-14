'''
Nama    : Zaidan Nur Muhammad Daffa
NIM     : 202410101080
Kelas   : Algo C
'''
#program DNC untuk Maximum Contiguous Subsequence Sum menggunakan fungsi rekursif

Input_num_list = input("Masukkan deret bilangan : ").split(",")


def devide(deret):
    if len(deret) == 1:
        return int(deret[0])
    elif len(deret)%2 ==0:
        batas = int(len(deret)/2)
        kiri = deret[:batas]
        kanan = deret[batas:]

        nilai_kiri = nilai("kiri",kiri)
        nilai_kanan = nilai("kanan",kanan)
        nilai_kiri_dan_kanan = nilai_kiri + nilai_kanan
        Hasil = max(nilai_kiri,nilai_kanan,nilai_kiri_dan_kanan)
        return max(Hasil,devide(kiri),devide(kanan))        
    elif len(deret)%2 != 0:
        batas = int(len(deret)//2)
        kiri = deret[:batas]
        kanan = deret[batas:]

        nilai_kiri = nilai("kiri",kiri)
        nilai_kanan = nilai("kanan",kanan)
        nilai_kiri_dan_kanan = nilai_kiri + nilai_kanan
        Hasil = max(nilai_kiri,nilai_kanan,nilai_kiri_dan_kanan)
        return max(Hasil,devide(kiri),devide(kanan))
        
def nilai(bagian,deret):
    if bagian == "kiri":
        deret.reverse()
        a = 0
        b = 0
        for i in deret:
            b= b + int(i)
            if b > a:
                a = b
        return a
    elif bagian =="kanan":
        a =0
        b = 0
        for i in deret:
            b= b + int(i)
            if b > a:
                a = b
        return a

print(f"Nilai penjumlahan maksimal deret tersebut adalah {devide(Input_num_list)}")