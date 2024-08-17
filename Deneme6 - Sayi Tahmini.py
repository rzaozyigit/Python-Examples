import random
rast = random.randint(1,100)
tahmin = int(input("Tuttugum sayiyi tahmin ediniz: "))
hak = 0
while hak < 6:
 if (rast != tahmin):
    if rast < tahmin:
        print("sayı daha aşşağı bir değer")
        hak += 1
        print("kalan tahmin hakkınız: {}".format(7-hak))
        tahmin = int(input("Tuttugum sayiyi tahmin ediniz: "))
    elif rast > tahmin:
        print("sayı daha yukarıda bir değer")
        hak += 1
        print("kalan tahmin hakkınız: {}".format(7-hak))
        tahmin = int(input("Tuttugum sayiyi tahmin ediniz: "))

 if rast == tahmin:
    print("Tahmininiz Dogru!")
    print("Tuttugum sayi: {}".format(rast))
    break
if hak >= 6:
 print("Tahmin hakkınız doldu :( ")
 print("Tuttugum sayi: {} ".format(rast))
