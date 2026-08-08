# Demonstrasi Kondisi, Operator Logika, 'in', 'is', dan Loop

# 1. Perbandingan Perbedaan Operator == dan is
x = [1, 2, 3]
y = [1, 2, 3]
print("x == y:", x == y)  # Membandingkan nilai
print("x is y:", x is y)  # Membandingkan identitas objek

# 2. Operator Boolean and, or, in
name = "John"
age = 23

if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")

if name in ["John", "Rick"]:
    print("Nama ditemukan dalam daftar pengguna.")

# 3. Operator Not
print("not False:", not False)
print("(not False) == (False):", (not False) == (False))

# 4. Loop Bilangan Prima / List
primes = [2, 3, 5, 7]
print("Cetak bilangan prima dalam list:")
for prime in primes:
    print(prime)
