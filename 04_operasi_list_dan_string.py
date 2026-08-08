# Demonstrasi Operasi List dan Format String

# 1. Operasi List Dasar
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)

print("Elemen list indeks 0:", mylist[0])
print("Elemen list indeks 1:", mylist[1])
print("Elemen list indeks 2:", mylist[2])

print("Iterasi semua elemen list:")
for x in mylist:
    print(x)

# 2. Operasi String
helloworld = "hello" + " " + "world"
print("String concatenation:", helloworld)

lotsofhellos = "hello" * 10
print("Perkalian string:", lotsofhellos)

# 3. Digabungkan List Ganjil Genap
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print("Gabungan list ganjil dan genap:", all_numbers)

# 4. String Formatting Gaya C
name = "John"
print("Hello, %s!" % name)
print("A list: %s" % mylist)
