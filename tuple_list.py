tuple_list = ( "ayşe", "fatma", "hasan", True , False , 123, 5454, 5645646, 4654, 54) #Listeler değiştirilebilir ancak tuple'lar değiştirilemez.
list_list = [ "ayşe", "fatma", "hasan", True , False , 123, 5454, 5645646, 4654, 54]

print("1_________________")
print(tuple_list) 
print(type(tuple_list))
print(dir(tuple_list))


print("_"*100)
print(dir(list_list))


print("2_________________")

print(len(tuple_list)) #Tuple'ın uzunluğunu verir

print("3_________________")
print(tuple_list.count("fatma")) #Belirtilen elemanın tuple içerisinde kaç tane olduğunu gösterir

print("4_________________")
print(tuple_list.index(True)) #Belirtilen elemanın index numarasını verir






