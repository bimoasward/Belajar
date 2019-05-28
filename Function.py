# Function.py

def hello():
    print("Hello")

hello
hello()

help(hello)

def hello(name):
    """
    Created By: Bimo
    Input: None
    Output: Hello

    """
    print("Hello " + name)

hello("Budi Luhur")

def hello(name="Budi Luhur"):
    print("Hello " + name)

# hello()
hello("Sakti")

def hitung(a,b):
    return a*b

# hitung()
hitung(5,6)
x = hitung(5,6)
print(x)

def hitung(a=5,b=4):
    return a*b

hitung()
print(hitung())
print(hitung(2,3))