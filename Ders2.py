import random
password = ("+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

paass = int(input("Şifre ne kadar uzun olsun?"))
sifre = ""
for i in range(paass):
    sifre += random.choice(password)

print(sifre)
