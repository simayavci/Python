sayi=int(input("Sayıyı giriniz: "))
i=1
toplam=0
while (i<sayi):
    if(sayi%i==0):
        toplam+=i
    i+=1
if(toplam==sayi):
    print("{} sayisi mukemmeldir".format(sayi))
else:
    print("{} sayisi mukemmel degildir".format(sayi))

