Bakiye = (2000)
para_cekme=1
para_yatirma=2
kart_bilgisi=3
kart_iade=4
islem = int(input("Yapmak istediğiniz işlemi seçiniz:"))
while islem == 1 or islem == 2 or islem == 3 or islem == 4:
    if islem ==1:
     tutar = int(input("Çekmek istediğiniz istediğiniz tutarı giriniz:"))
     if tutar >= Bakiye:
        print("Yetersiz Bakiye")
     else:
        Bakiye -= tutar
        print("Bakiyeniz = {}".format(Bakiye))
        islem = int(input("Yapmak istediğiniz işlemi seçiniz"))
    elif islem == 2:
      tutar = int(input("Yatırmak istediğiniz istediğiniz tutarı giriniz:"))
      Bakiye += tutar
      print("Bakiyeniz = {}".format(Bakiye))
      islem = int(input("Yapmak istediğiniz işlemi seçiniz"))
    elif islem == 3:
      kart_bilgileri=["Rıza Özyiğit","Iban = TR6400015648","Kalan Bakiyeniz = {}".format(Bakiye)]
      print(kart_bilgileri)
      islem = int(input("Yapmak istediğiniz işlemi seçiniz"))
    elif islem==4:
        print("Kartınız iade edildi")
        break
