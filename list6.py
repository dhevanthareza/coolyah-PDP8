"""
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
"""
numbers = input("Masukan Angka pisahkan dengan spasi = ").split(" ")
genapCount = 0
for i in numbers:
    if(int(i) % 2 == 0): genapCount += 1
    if(genapCount == 2 ): 
        print("{} terdapat pada index ke-{}".format(i, numbers.index(i)))
        break