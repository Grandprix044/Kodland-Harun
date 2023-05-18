direkt = {
    "LOL": "komik bir şeye verilen cevap",
    "CRINGE": "garip ya da utandırıcı bir şey",
    "ROFL": "bir şakaya karşılık cevap",
    "SHEESH": "onaylamamak",
    "CREEPY": "korkunç",
    "AGGRO": "agresifleşmek/sinirlenmek"
}

cıktı = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

if cıktı in direkt.keys():
    print(direkt[cıktı])
else:
    print("Anlaşılmadı")
