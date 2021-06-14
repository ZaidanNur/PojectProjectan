from itertools import permutations
#1. Hitung harga antar titik pada setiap grafnya

Graf_soal = [[0,10,15,20],
             [10,0,35,25],
             [15,35,0,30],
             [20,25,30,0]]
#2. Tentuka titik start nya
# start di buat 0 karena start di mulai dari titik 1
Starting_point = 0

#3. Buat fungsi TSP-nya
def tsp(graf,sp):
    node= [] #titik yang dituju/ urutan jalannya graf
    for i in range(len(Graf_soal)):
        if i != Starting_point:
            node.append(i)
    
    min_cost = 99999999 #digunakan untuk perbandingan graf paling minium
    next_path = permutations(node) # Cari permutasi dari node yang ada
    all_cost = []
    all_path = []

    for i in next_path: #harus pake for biar bisa kebaca
        current_cost = 0 #Menampung cost saat ini
        S1 = Starting_point #Start point, pada awalnya diset sesuai titik mulai\

        for j in i: #Mencari jarak antara titik hasil permutasi
            current_cost += Graf_soal[S1][j]
            S1 = j #Agar nilainya dinamis, nilai S1 diganti dengan nilai titik saat ini

        current_cost += Graf_soal[S1][Starting_point] #Menambahkan cost titik akhir dengan starting point
        all_cost.append(current_cost)
        all_path.append(i)

    min_cost = min(all_cost)
    location = [i for i, val in enumerate(all_cost) if val==min_cost] #
    print("Path(s) with minimal cost :")
    for i in location:
        print(all_path[i])

    return min_cost

print(f"Minimal cost : {tsp(Graf_soal,Starting_point)}")
