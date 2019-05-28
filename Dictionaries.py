# Dictionaries.py

fruits = {"Apple":8, "Jeruk":6, "Melon":11}
print(fruits)
print(fruits['Apple'])

new_dict = {"Key1":15, "Key2":[19, 79, 20], "Key3":fruits}
print(new_dict)
print(new_dict["Key1"])
print(new_dict["Key2"][1])
print(new_dict["Key3"])
print(new_dict["Key3"]["Apple"])