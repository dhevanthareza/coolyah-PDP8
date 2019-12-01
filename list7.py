"""
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
"""
numbers = input("Masukan Angka pisahkan dengan spasi = ").split(" ")
for i in numbers[::-1]:
    if(int(i) % 2 != 0):
        print("{} terdapat pada index ke-{}".format(i, numbers.index(i)))
        break