Vize1=int(input("1. Vize notunuzu giriniz: "))
Vize2=int(input("2. Vize notunuzu giriniz: "))
Final=int(input("Final notunuzu giriniz: "))
sonuc=0.3*Vize1+0.3*Vize2+0.4*Final
if sonuc>=80:
    print("Notunuz AA")
elif sonuc<80 and sonuc>=60:
    print("Notunuz BB")
elif sonuc<60 and sonuc>=40:
    print("Notunuz CC")
elif sonuc<40 and sonuc>=20:
    print("Notunuz DD")
else:
    print("Notunuz FF")