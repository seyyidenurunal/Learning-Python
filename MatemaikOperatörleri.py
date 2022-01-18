#Değişkenleri tanımlayalım.

x = 54  # İnteger - Tamsayı
y = 48
z = 91

print("x + y + z")  #Toplama
print(x + y + z)

print("(x - y - z") #Çıkarma
print(x - y - z)

print("x * y * z") #Çarpma
print(x * y * z)

print("z / y / x") #Bölme
print(z / y / x)


p = 5.8 # Float = Kesirli sayılar
t = 2.5
k = 4.5


print("p + t + k")
print(p + t + k) 


i = 8 # Bir değişken tanımladık ve bnu bir artırmak istiyoruz

#i = i + 1 

i += 1 # Kısa yolu

print("i")
print(i)

#Bunu diğer işlemlerde de deneyelim

s = 7

s *= 2 

print("s")
print(s)

m = 535
f = 25

print("m/f")
print(m / f) #bölme işlemi
print("Tamsayı bölmesi m // f")
print(m // f) #Yapılan işlemin sonucu kesirli olsa bile tamsayı olarak verir.

g = 58
n = 4 

print("g'nin n ile bölümünden kalan =")
print(g % n) #Kalanı bulma


j = 4
c = 8  
d = 0.5

# j^c
print("j^c")
print(j ** c) # Üs bulma = Soldaki sayının sağdaki sayıya göre üssünü yazar.

print("j karekök")
print(j ** d)

#İşlem Önceliği:
print(5 * 22 / 2 + 5 - 8 / 4 * 2)
print(((5 * 22) / 2) + 5 - ((8 / 4) * 2))