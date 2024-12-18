 # operasi aritmatika

a = 10
b = 3

# operasi tambah (+)
hasil = a + b
print(a, "+", b, "=", hasil)
# operasi kurang (-)
hasil = a - b
print(a, "-", b, "=", hasil)
# operasi kali (*)
hasil = a * b
print(a, "*", b, "=", hasil)
# operasi pembagian (/)
hasil = a / b
print(a, "/", b, "=", hasil)
# operasi pembagian bulat/floor division (//)
hasil = a // b
print(a, "//", b, "=", hasil)
# operasi modulasi/sisa pembagian (%)
hasil = a % b
print(a, "%", b, "=", hasil)
# operasi pemangkatan/exponen (**)
hasil = a ** b
print(a, "**", b, "=", hasil)

# prioritas operasi aritmatika

"""
1. ()
2. *, **, /, %, //
3. +, -
"""
x = 3
y = 2
z = 4

hasil = x**y * (z + x) / y - y % z // x
print(hasil)