print("1____________") 

while True:
    isim = input("İsim : (Çıkmak için 'q'ya basın): ")
    if (isim == "q"):
        print("Programdan çıkılıyor...")
        break
    print("İsminiz : ", isim)

print("2____________") 

for i in range(0,11):
    print("i : ", i)

print("3____________") 

for i in range(0,11):
    if (i == 3 or i == 5):
        continue
    print("i : ", i)

