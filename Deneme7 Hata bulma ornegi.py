while True:
    try:
        boy = float(input("lütfen boyunuzu Metre cinsinden giriniz(örnek: 1.85): "))
        break
    except ValueError:
        print("Lütfen sayıyı doğru giriniz!")
while True:
    try:
        kütle = float(input("lütfen kütlenizi kg cinsinden giriniz(örnek: 75): "))
        break
    except ValueError:
        print("Lütfen sayıyı doğru giriniz!")

print(kütle / boy ** 2)