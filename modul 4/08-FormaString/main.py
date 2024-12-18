# format string
"""
  sting : kumpulan dari karakter
  cara membuat string :
  1. dengan single quote '...'
  2. dengan double quote "..."
"""

# membuat string dengan single quote
nama = 'nama saya zenitsu agatsuma'
print(nama)

# membuat string dengan double quote
# di gunakan ketika ada penguunaan tanda petik (')
nama = "nama saya inosuke ha'shibara"
print(nama)

# ketika maksa untuk menggunakan single quote
# harus menggunakan tanda(\)
print('nama saya ma\'put')
# sedangkan jika ada tanda (\) di teksnya maka tinggal ditambahkan lagi tandanya
print('c:\\user\\mizii')

nama = "mizii"
print("selamat datang", nama)

# format string 'f' dan '{}'
format_str = f'selamat datang {nama}'
print(format_str)

# format string angka 
angka = 2005.5
format_str = f'angka = {angka}'
print(format_str)

# bilangan dengan ordo ribuan
angka = 2000000
format_str = f'jutaan = {angka:,}'
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f'desimal = {angka:.3f}'
print(format_str)

# persen
angka = 0.55
format_str = f'persen = {angka:%}'
print(format_str)

angka = 0.55
format_str = f'persen = {angka:.1%}'
print(format_str)

# melakukan operasi aritmatika dengan format string

harga = 57250
jumlah = 3

print(f'total bayar : {harga * jumlah :,}')