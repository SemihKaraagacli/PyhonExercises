# "Verilen üç sayının en büyüğünü bulan bir Python kodu yazınız."



sayilarListesi=[]

adet = int(input("Kaç Sayı Girilecek: "))

for i in range(adet):
    sayilar = int(input("Lütfen birkaç değer giriniz: "))
    sayilarListesi.append(sayilar)

enkucukDeger =  min(sayilarListesi)
enbuyukDeger = max(sayilarListesi)

print("Girilen değerlerin en büyüğü: ",enbuyukDeger, " \n Girilen değerlerin en küçüğü: "  ,enkucukDeger)