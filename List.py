# List.py

first_list = ["Salam", 10, 19.79]
print(first_list)

second_list = ["Budi", "luhur", "Sakti"]
print(second_list)

print(first_list, second_list)

new_list = first_list + second_list
print(new_list)

empty_list = []
print(empty_list)

mhs = ["Budi", "luhur", "Sakti"]
print(mhs)
print(mhs[0])   #Isi List Index ke 0
print(mhs[-1])  #Isi List Index ke -1 dari akhir
print(mhs[0:2]) #Isi List Index mulai ke 0 sebanyak 2

mhs.append("Baru")  #Tambah ke list mhs
print(mhs)