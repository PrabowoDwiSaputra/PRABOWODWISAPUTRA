# operasi komparasi/pembandingan

#perhatikan!!
"""
hasil dari operasi komparasi 
selalu bertipe data boolean
(true/false)
"""
# >, <, >=,<=, ==, !=, is, dan is not

a = 4
b = 2

# lebih dari(>)
print("lebih dari (>)")
hasil = a > 3 # true
print(a, ">", 3, "=", hasil)

# kurang dari (<)
hasil = a < 3 # false
print(a, "<", 3, "=", hasil)

# hasil tetap sama dengan false
hasil = b > 2 # false
print(b, ">", 2, "=", hasil)

# lebih dari sama dengan (>=)
hasil = a >= 3 # true
print(a, ">=", 3, "=", hasil)

# kurang dari sama dengan (<=)
hasil = a <= 3 # false
print(a, "<=", 3, "=", hasil)

# sama dengan (==) operator perbandingan
hasil = a == 3 # false
print(a, "==", 3, "=", hasil)

# tidak sama dengan (!=)
hasil = a != 3 # true
print(a, "!=", 3, "=", hasil)

# hasil dari nilai b
hasil = b >= 3 # false
print(b, ">=", 3, "=", hasil)
hasil = b <= 3 # true
print(b, "<=", 3, "=", hasil)
hasil = b == 3 # false
print(b, "==", 3, "=", hasil)
hasil = b != 3 # true
print(b, "!=", 3, "=", hasil)

hasil = a is 3 
print(a, "is", 3, "=", hasil)
hasil = a is not 3 
print(a, "is not", 3, "=", hasil)

hasil = b is 3 
print(b, "is", 3, "=", hasil)
hasil = b is not 3 
print(b, "is not", 3, "=", hasil)