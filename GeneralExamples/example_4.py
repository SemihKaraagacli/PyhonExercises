# "Örnek1: Bir sayının pozitif mi negatif mi sıfır mı olduğunu bulan kadu yaz"

a = float(input("Lütfen bir değer giriniz: "))

if a > 0:
    print("Girilen değer 'pozitif' bir değerdir.")
elif a == 0:
    print("Girilen değer '0' eşittir.")
elif a < 0:
    print("Girilen değer 'negatif' bir değerdir.")