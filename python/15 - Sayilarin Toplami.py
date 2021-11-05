toplam=0
while True:
    sayi=input("Sayiyi giriniz: ")
    if(sayi=="q"):
        print("Programdan cikiliyor..")
        break
    sayi=int(sayi)
    toplam+=sayi
print("Sayilarin toplamı: {} ".format(toplam))


