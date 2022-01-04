liste = [ "elma", "armut", "portakal" ]

print("1____________") 
for item in liste:  #Liste içerisindeki elemanları tek tek yazmayı sağlar.
    print(item)

print("2____________") 
sayi = [1, 87, 1, 178, 28, 17, 658, 829]

total=0

for toplam in sayi:
   total= total+ toplam

print(total)  #sayi listesinin içindeki sayıların toplamı

print("3____________") 
for say in sayi:
    print(say) # Sayıları alt alta sıralar.

print("4____________") 
print(list(range(10))) #0'dan 9'a kadar rakamların yer aldığı bir liste oluşturur.

print("5____________") 
for item in range(10): #0'dan 9'a kadar rakamları alt alta sıralar.
    print(item)

print("6____________") 
for item in range(100):
    if item % 2 == 0:  # 99'a kadar olan çift sayıları alt alta sıralar.
        print(item) 

print("7____________") 
isim = "Ayşe"
for harf in isim:  
    print(harf) # İsimdeki harfleri yukarıdan aşağı sıralar.

    