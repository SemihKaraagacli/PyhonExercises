# Bir otoparkın ücret tarifesi aşağıdaki gibidir:

# 1 saate kadar: 5 TL
# 1-5 saat arası: Saat başı 4 TL
# 5 saatten fazla: Saat başı 3 TL
# # Buna göre kullanıcının girdiği otoparkta kalınan saat süresine göre ödenecek miktarı bularak ekrana yazdır



a = float(input("Otopark da kaç saat duruldu ?"))


if a == 1 :
    print("Ücretiniz 5 TL")
elif 1< a <= 5:
    b = str(a * 4)
    print ("Ücretiniz: " + b )
elif 5<a :
    c = str(a * 3)
    print("Ücretiniz: " + c)
