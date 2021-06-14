'''
Nama    : Zaidan Nur Muhammad Daffa
NIM     : 202410101080
Kelas   : Algo C
'''
#program DNC untuk Maximum Contiguous Subsequence Sum menggunakan algoritma Kadane
Input_deret = input("Masukkan deret bilangan : ").split(",")

def nilai_maks(deret,indeks,panjang,nilaisekarang=0,nilaimaks=0):
    if indeks == (panjang):
        print(f"Nilai maksimal dari deret tersebut adalah {nilaimaks}")
        return nilaimaks
    elif indeks == 0:
        nilaisekarang = int(deret[indeks])
        nilaimaks = nilaisekarang
        if nilaisekarang < 0:
            nilaisekarang = 0
        nilai_maks(deret,indeks+1,panjang,nilaisekarang,nilaimaks)
    else:
        nilaisekarang = nilaisekarang +  int(deret[indeks]) # -2,11,-4,13,-4,2
        if nilaisekarang < 0:
            nilaisekarang = 0
        if nilaisekarang > nilaimaks:
            nilaimaks = nilaisekarang
        nilai_maks(deret,indeks+1,panjang,nilaisekarang,nilaimaks)
        
nilai_maks(Input_deret,0,len(Input_deret))
