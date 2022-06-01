# "Soru: Bir bankada mühendis olarak çalışıyorsun. Müşteri için parola belirleme kriterleri oluşturmanız"
# "bekleniyor. Örneğin en az 8 karakterden oluşması, içinde en az bir büyük harf ve en az bir rakam olması"
# "gibi kriterler koyabilirsiniz. Bu kriterler ve bunlara uyan ya da uymayan yanıtları içeren beş ayrı kod yaz"



a = input("Parola Giriniz: ")

if len(a) >= 8:
    if a.lower() != a != a.upper():
        print("Parola kaydedildi.")
    else:
        print("Parolanızda en az 1 büyük, 1 küçük harf olamlıdır.")
else:
    print("En az 8 karakterli ve en az 1 büyük, 1 küçük harf olamlıdır.")

