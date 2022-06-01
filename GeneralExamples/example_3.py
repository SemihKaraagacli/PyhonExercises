# "ÖRNEK: Bir üçgenin eşkenar, ikizkenar veya eşkenar olmayan olup olmadığını kontrol eden bir "
# "Python programı yazın"

a = int(input("[AB] Birim Değerini Giriniz: "))
b = int(input("[AC] Birim Değerini Giriniz: "))
c = int(input("[BC] Birim Değerini Giriniz: "))

if a == b == c:
    print("[ABC] üçgeni bir eşkenar ücgendir.")
elif a == b or a == c or b == c:
    print("[ABC] üçgeni bir ikizkenar ücgendir.")
else:
    print("[ABC] üçgeni eşkenar ya da ikizkenar üçgen değildir.")
