print("1____________") 

list1 = [1,2,3,4,5]
list11 = [i for i in list1] #List1'deki elemanları list11'e eklemeye yarar.

print(list11)

print("2____________") 

list3 = [3,4,5]
list33 =[i * 2 for i in list3] # List3'teki elemanları 2 ile çarparak list 33'e ekler.

print(list33)

print("3____________") 

list5 = [(1,2),(3,4),(5,6),(7,8)] 
list55 = [i * j for i, j in list5] #Demetler içerisindeki elemanları birbiri ile çarparak list55'e ekler.

print(list55)

print("4____________") 

s = "Python"
list6 = [i * 3 for i in s] #String içerisindeki harflerin her birini 3 ile çarparak list6'ya ekler. 'ppp' gibi.

print(list6)

print("5____________") 

list7 = [(1,2,3),(4,5,6,7),(8,9,10,11,12,13)]
list77 = [x for i in list7 for x in i] # liste içerisindeki demetlerin içinde de tek tek gezinmeyi ve bunları list77'e eklemeyi sağlar.

print(list77)


