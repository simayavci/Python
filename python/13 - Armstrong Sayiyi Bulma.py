sayi=input("Sayiyi giriniz: ")
basamak=0
toplam=0
basamak_sayisi=len(sayi)
sayi=int(sayi)

gecici=sayi
while(gecici>0):
    basamak=gecici%10
    toplam+= basamak**basamak_sayisi
    gecici//=10

if(sayi==toplam):
    print("{} armstrong sayisidir".format(sayi))
else:
    print("{} armstrong sayisi degildir".format(sayi))
    


