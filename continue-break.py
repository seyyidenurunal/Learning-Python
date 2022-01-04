baslangic = 0

while  baslangic < 10:
   baslangic = baslangic + 1
   if baslangic  % 2 != 0:
      continue
   print(baslangic)
       

 
while  baslangic < 10:
   baslangic = baslangic + 1
   if baslangic  % 2 == 0:
      continue
   print(baslangic)


while True:
   alinan = input("iSMİ BULUNUZ.")
   if alinan == "ÇIKIŞ":
      break 
print(alinan)