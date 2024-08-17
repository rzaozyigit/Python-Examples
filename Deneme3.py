sayi= int(input("Bir Sayi Giriniz"))

fact=1
for i in range(1,sayi+1):
    fact = fact * i

print("{}! = ".format(sayi)+str(fact))