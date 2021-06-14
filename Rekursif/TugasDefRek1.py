import  os

Input_user = int(input("Masukkan jumlah menu : ")) # Memasukkan jumala menu
Data = list() # Menampung menu
# Data = [["1","0","Menu_1"],["2","1","Menu_2"]]
#3 -> (3 -1 ) -> (3-1)-1 -> (3-1)-1)-1 -> n = 0
def menu(n=Input_user,Parent=None,identitas=None): # fungsi buat menu
    if n == 0: # Awal masuk berniali FALSE
        for i in Data:
            # i = ["1","0","Menu_1"]
            #   "0"     "0"   -> True
            if i[1] == str(Parent):
                jarak ="....."
                print(f"{jarak*identitas}{i[2]}")
                Parent1 = i[0] # -> kita cari keluarga
                identitas1 = identitas+1 # n = 0
                menu(n,Parent1,identitas1)
    else:
        Input_menu = input("Menu : ").split(" ") # 1 0 menu_1
        # Aku sayang kamu -> ["Aku","sayang","kamu"]
        Data.append(Input_menu)
        os.system("cls")
        menu(n-1,Parent,identitas)

menu(Parent="0",identitas= 0)

#3 main3
