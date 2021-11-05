print("""*******************************
-----Basit Hesap Makinesi-----

1. Toplama
2. Çıkartma
3. Çarpma
4. Bölme

""")
islem=input("İşlemi Giriniz: ")
s1=float(input("1. Sayıyı Giriniz: "))
s2=float(input("2. Sayıyı Giriniz: "))

if islem=="1":
    print("{} + {} = {} ".format(s1,s2,s1+s2))
elif islem=="2":
    print("{} - {} = {} ".format(s1,s2,s1-s2))
elif islem=="3":
    print("{} * {} = {} ".format(s1,s2,s1*s2))
elif islem=="4":
    print("{} / {} = {} ".format(s1,s2,s1/s2))
else:
    print("Hatalı işlem girdiniz!")
