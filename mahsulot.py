mahsulotlar = {"non": 4000, "sut": 12000, "olma": 8000}

mahsulot_nomi = input("Mahsulot nomi: ")
yangi_narx = int(input("Yangi narx: "))

if mahsulot_nomi in mahsulotlar:
    mahsulotlar[mahsulot_nomi] = yangi_narx
    print("Narx yangilandi")
    print(mahsulotlar)
else:
    print("Mahsulot topilmadi.")