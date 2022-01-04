pazar = ["elma", "kiraz", "muz", "çilek", "üzüm", "karpuz", "elma", "kivi", "kivi", "elma"]  #Aynı elemanı birden fazla yazabilirsiniz
                                                                                             #Kümeler ile arasındaki farklardan biri budur.


print("1____________") 
print(pazar)

print("2____________") 
print(pazar[2]) #muz

print("3____________") 
print(pazar[-4]) #üzüm

print("4____________") 
pazar.append("kiraz")
print(pazar)

print("5____________") 
yeni = pazar[1:4]  # İki noktadan önceki sayı alınacak ilk elemanı, iki noktadan sonraki sayı da alınacak elemandan bir sonraki elemanın sayısını verir
print(yeni)
yeni_1 = pazar[2:]  # İkici elemandan(muz) sonraki bütün elemanları alır.
print(yeni_1)
yeni_2 = pazar[:3]  # Üçüncü elemandan(çilek) önceki bütün elemanları alır.

print("6____________")
esya = [ "sandalye", "masa", "koltuk", "halı", "perde"]
print(pazar + esya)

print("7____________") 
esya.clear()
print(esya)

print("8____________") 
print(pazar.count("elma")) # Kaç tane elma elemanı olduğunu gösterir.

print("9____________") 
print(pazar.index("üzüm")) #Kaçıncı index numarasında olduğunu gösterir. Üzüm 4. index numarasındadır.i
                           #Aynı değere sahip elemanlar için, önce gelen elemanın index numarasını verir. Örneğin; elma : 1 
print("8____________") 
pazar.pop() #Son elemanı listeden atar. 4 Numarada listeye kiraz elemanını eklemiştik, onun listede çıkması gerekir.

print("10____________") 
pazar.remove("üzüm") #Seçilen elemanı listeden atar.  
print(pazar)

print("8____________") 
pazar.reverse() #listeyi tersine çevirir.
print(pazar)

print("8____________") 
pazar.sort() #Alfabetik olarak sıralar.
print(pazar)