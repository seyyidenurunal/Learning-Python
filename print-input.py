isim = input("LÜTFEN İSİM GİRİNİZ.") # İnput fonksiyonu kullanıcıdan bir değer almayı sağlar.
soyisim = input("LÜTFEN SOYİSİM GİRİNİZ.")
yas = int(input("YAŞINIZI GİRİNİZ."))


print(isim + " " + soyisim + " " + str(yas)) 

print("Merhaba\nNe Haber\nNasılsın?") #\n kaarakteri string ifadelerde bir alt satıra geçmeyi sağlar.

print("Ali\tAyşe\tMerve") # \t Karakteri string içerisinde bulunduğu yerde bir tab boşluk bırakır.

print(25,65,11,75,77, sep = "/") # sep parametresi, değerler arasına boşluk yerine belirlenen karakterin konulmasını sağlar.

print("Bugün", "Günlerden", "SALI", sep = "\n") 

print(*"Hello") #Stringin başına * koyarsak her bir harfi ayırarak aralarına boşluk koyar.

print(*"Hello", sep = "\n") # Bu şekilde her bir harf alt alta yazılmış olur.

#FORMAT FONKSİYONU
#https://pyformat.info/ format fonsiyonunun kullanımlarını bulmak için bu siteyi ziyaret edebilirsiniz.

x = 5
y = 7

print("{} ile {} 'nin çarpımı {} eder".format(x,y, x*y)) #Format fonsiyonu süslü parantezler içerisine hangi değerlerin geleceğini gösteriyor.
                                                        
