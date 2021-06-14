vocal_letter = "aiueo"
Input_user = input("Masukkan kaliamat : ")
Vowels = []
Consonants = [] 
spasi = []



for i in Input_user:
    if i in vocal_letter:
        Vowels.append(i)
    elif i.isspace() == True:
        spasi.append(i)
    else :
        Consonants.append(i)
print(f"Jumlah huruf vokal : {len(Vowels)}")
print(f"Jumlah huruf konsonan : {len(Consonants)}")
print(f"Jumlah spasi : {len(spasi)}")


