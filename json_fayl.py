import json

with open("products.json", "r") as f:
    mahsulotlar = json.load(f)


nom = input("Mahsulot nomi: ")
yangi_miqdor = int(input("Yangi miqdor: "))

topildi = False

for mahsulot in mahsulotlar:
    if mahsulot["nom"] == nom:
        mahsulot["miqdor"] = yangi_miqdor
        topildi = True
        break

if topildi:
    with open("products.json", "w") as f:
        json.dump(mahsulotlar, f, ensure_ascii=False, indent=4)

    print("Mahsulot miqdori muvaffaqiyatli yangilandi!")
else:
    print("Bunday mahsulot topilmadi!")
