import csv

mahsulotlar = [
    ["Olma", 8000, 12],
    ["Non", 4000, 20],
    ["Sut", 14000, 5]
]

with open("products.csv", "w") as f:
    yozish = csv.writer(f)
    yozish.writerow(["nom", "narx", "soni"])
    yozish.writerows(mahsulotlar)

print("Ma'lumotlar products.csv fayliga yozildi!")
