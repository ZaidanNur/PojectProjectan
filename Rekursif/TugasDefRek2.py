Input_user = input("Masukkan kalimat :")
def palindrome(text=Input_user):
    dictio = {""}
    text= text.translate({ord(i):None for i in ". ,"}).lower()
    return len(text) < 2 or text[0] == text[-1] and palindrome(text[1:-1])
palindrome()
if palindrome() == True:
    print("Kalimat tersebut palindrom")
else:
    print("Kalimat tersebut bukan palindrom")

# ndadndjasndiasndian 1. huruf e lowercase kabeh, tanda baca & spasi di ilangi
# "n" == "n"
# text = "dadndjasndiasndia"
# text =
# 2 