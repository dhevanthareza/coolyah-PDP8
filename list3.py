"""
NAMA        : DHEVAN MUHAMAD ANTHAREZA
NIM         : A11.2019.12293
KELOMPOK    : A11.4118
"""
datas = []
while True :
    datas.append(float(input("Masukan data ke-{} = ".format(len(datas)))))
    if (input("apakah anda ingin input lagi = ") in ("N", "n")): break
search = float(input("angka yang dicari = "))
print('Data ditemukan' if search in datas else 'Data tidak ditemukan')