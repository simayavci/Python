kilo=float(input("Kilonuzu giriniz: "))
boy=float(input("Boyunuzu giriniz: "))
bki=kilo/boy**2

if bki<18.5:
    print("Zayıf")
elif(bki>18.5 and bki<25):
    print("Normal")
elif(bki>25 and bki<30):
    print("Fazla Kilolu")
else:
    print("Obez")
