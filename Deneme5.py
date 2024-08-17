gelensayi = int(input("Bir sayi giriniz:"))
def tamsayibolenial(sayi):
    bosListe = []
    for i in range(1,sayi):
        if sayi % i == 0:
            bosListe.append(i)
    return bosListe

print(tamsayibolenial(gelensayi))