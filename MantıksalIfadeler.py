#True and True = True 
#True and False = False
#False and False = False
#False and False = False

#True or True = True 
#True or False = True
#False or False = True
#False or False = True


isim = input("KULLANICI ADI: ")
sifre = input("ŞİFRE: ")

print( isim == "Ayşe Nur" and sifre == "123456")  #Kullanıcı adı ve şifre belirtildiği gibi ise True gelir.

print( isim == "Ayşe Nur" or sifre == "123456")   #Kullanıcı adı ve şifreden yalnız biri doğru ise True gelir.

print(not(isim == "Fatma")) #Kullanıcı adı Ayşe ise False gelir.