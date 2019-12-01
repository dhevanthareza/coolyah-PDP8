"""
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
"""
numbers = input("Masukan Angka pisahkan dengan spasi = ").split(" ")
ganjilNumber = 0
index = 0
for ind, number in enumerate(numbers):
    if(int(number) % 2 != 0):
        ganjilNumber = number
        index = ind
print("{} terdapat pada index ke-{}".format(ganjilNumber, index))        