"""
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
"""
datas = []
while True :
    datas.append(float(input("Masukan data ke-{} = ".format(len(datas)))))
    if (input("apakah anda ingin input lagi = ") in ("N", "n")): break
for index, data in enumerate(datas) :
    print("Data di index ke-{} = {}".format(index, data))