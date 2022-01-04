alacaklar = set({"elma", "armut", "kiraz"})  #Verilerin sırası önemmli değildir. 
                                             #Bir sete aynı elemandan yalnızca bir tane ekler.
                                             #alacaklar = {"elma"} , bir diğer yazım şekli.


print("1____________") 
print(dir(alacaklar)) 

print("2____________") 
print(help(alacaklar.add)) #Ne işe yaradığını gösterir.

print("3____________") 
alacaklar.add("ev") #Kümenin içine eleman ekler.
alacaklar.add("araba")
alacaklar.add("kitap")
print(alacaklar)

print("4____________") 
alacaklar.remove("ev")
print(alacaklar)

print("5____________") 
alacaklar.clear()
print(alacaklar)

print("6____________") 
alacaklar.discard("armut") # Eleman varsa sil, yoksa hata verme.
print(alacaklar)

print("7____________") 
tek_sayilar = set([1,3,5,7,9])
cift_sayilar = set([2,4,6,8])
asal_sayilar = set([2,3,5,7])

print(cift_sayilar.union(tek_sayilar)) # Kümelerin birleşimi

print(tek_sayilar.intersection(asal_sayilar)) #Kümelerin kesişimi 
print(cift_sayilar.intersection(asal_sayilar))

