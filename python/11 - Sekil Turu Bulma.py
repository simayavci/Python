sekil=input("Şekil türünü giriniz: ")
if sekil=="Dortgen":
    print("Kenarları giriniz: ")
    a=int(input("1. Kenar: "))
    b=int(input("2. Kenar: "))
    c=int(input("3. Kenar: "))
    d=int(input("4. Kenar: "))
    if(a==b and a==c and a==d):
        print("Şekil karedir.")
    elif(a==b and c==d):
        print("Şekil dikdörtgendir.")
    elif(a==c and b==d):
        print("Şekil dikdörtgendir.")
    elif(a==d and b==c):
        print("Şekil dikdörtgendir.")
    else:
        print("Şekil dörtgendir.")
elif sekil=="Ucgen":
    
    print("Kenarları giriniz: ")
    a=int(input("1. Kenar: "))
    b=int(input("2. Kenar: "))
    c=int(input("3. Kenar: "))
    if(abs(a-b)<a and (a+b)>a)or (abs(a-c)<b and (a+c)>b)or (abs(b-c)<a and (c+b)>a):
        if(a==b and a==c):
            print("Şekil eşkenar üçgendir")
        elif((a==b and a!=c)or (a==c and a!=b)or (b==c and a!=c)):
            print("Şekil ikizkenar üçgendir")
        else:
            print("Şekil çeşitkenar üçgendir")
    else:
        print("Ucgen belirtmemektedir.")
else: 
    print("Tanimsiz sekil girdiniz")
    
    
    

    
