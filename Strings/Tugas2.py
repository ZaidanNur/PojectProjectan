Input_user = input("Masukkan kalimat : ")
Split_word = Input_user.split(" ")
Numeric = []
Upper = []
Lower = []

for i in Input_user:
    if i.isnumeric()== True:
        Numeric.append(i)
    elif i.isupper() == True:
        Upper.append(i)
    elif i.islower() == True:
        Lower.append(i)

print(f"Jumlah angka dalam kalimat {len(Numeric)}")
print(f"Jumlah kata dalam kalimat {len(Split_word)}")
print(f"Jumlah huruf besar dalam kalimat {len(Upper)}")
print(f"Jumlah huruf kecil kalimat {len(Lower)}")


