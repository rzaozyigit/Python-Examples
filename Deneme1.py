
ogrenci_listesi = {"ad":"ort"}

ad = input("adınızı yazınız")
vize = int(input("Vize Notunuzu Giriniz"))
final = int(input("Final Notunuzu Giriniz"))
ort = (vize*40/100)+(final*60/100)
if ort >=85:
    print("Sayın {0} sınav ortalamanız: {1} ortalamanıza göre harf notunuz: AA'dır. ".format((ad),(ort)))
elif ort >=70 and ort<=85:
    print("Sayın {0} sınav ortalamanız: {1} ortalamanıza göre harf notunuz: BA'dır. ".format((ad),(ort)))
elif ort >=60 and ort<=70:
    print("Sayın {0} sınav ortalamanız: {1} ortalamanıza göre harf notunuz: BB'dır. ".format((ad),(ort)))
elif ort >=50 and ort<=60:
    print("Sayın {0} sınav ortalamanız: {1} ortalamanıza göre harf notunuz: CB'dır. ".format((ad),(ort)))
elif ort >=40 and ort<=50:
    print("Sayın {0} sınav ortalamanız: {1} ortalamanıza göre harf notunuz: CC'dır. ".format((ad),(ort)))
else:
    print("Sayın {0} sınav ortalamanız: {1} ortalamanıza göre harf notunuz: FF'dır. ".format((ad),(ort)))
ogrenci_listesi=((ad),(ort))
print(ogrenci_listesi)