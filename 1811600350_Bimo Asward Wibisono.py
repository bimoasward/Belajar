# Tugas: Buat program untuk input data mahasiswa dengan kriteria sbb:
    # input jumlah mahasiswa
    # kemudian input data nim, nilai absen, nilai, tugas, nilai uts, nilai uas sejumlah mahasiwa yang diinput
    # hitung nilai akhir = 10%nilai absen + 20% nilai tugas + 30%nilai uts + 40%nilai uas
    # cari grade berdasarkan nilai akhir (NA), jika NA: 85-100: A, 80 - <85: A-, 75 - <80: B+, 70 - <75: B, 65 - <70: B-, 60 - <65: C, 45 - <60: D, 0 - <45: E
    # Cetak Seluruh Data Mahasiswa (NIM, Nilai Absen, Nilai Tugas, Nilai UTS, Nilai UAS, Nilai Akhir, Grade)
    # Cetak  Nilai Rata-rata Kelas
# Fungsi yang harus ada adalah: 
# HitungNilaiAkhir(params)
# KonversiGrade(params)

def HitungNilaiAkhir(a,b,c,d):
    return a * 10/100 + b * 20/100 + c * 30/100 + d * 40/100

def KonversiGrade(x):
    if x >= 85:
        return("A")
    elif x > 80:
        return("A-")
    elif x > 75:
        return("B+")
    elif x > 70:
        return("B")
    elif x > 65:
        return("B-")
    elif x > 60:
        return("C")
    elif x > 45:
        return("D")
    else:
        return("E")

print('----------------------------------------------------')
print('Nim \t: 1811600350')
print('Nama \t: Bimo Asward Wibisono')
print('Kelas \t: XM')
print('Tugas \t: Data Sains')
print('Tugas \t: Input Data Mahasiswa')
print('----------------------------------------------------')

jml_mhs = input("Input jumlah mahasiswa: ")
jml_mhs = int(jml_mhs)
total_nilai = 0
i=0
mahasiswa = dict()
while i<jml_mhs:
    print("\nUntuk Mahasiswa ke", i+1)
    nim_mhs = input("Nim: ")
    nilai_absen_mhs = int(input("Nilai absen: "))
    nilai_tugas_mhs = int(input("Nilai tugas: "))
    nilai_uts_mhs = int(input("Nilai uts: "))
    nilai_uas_mhs = int(input("Nilai uas: "))
    nilai_akhir_mhs = int(HitungNilaiAkhir(nilai_absen_mhs,nilai_tugas_mhs,nilai_uts_mhs,nilai_uas_mhs))
    nilai_grade_mhs = KonversiGrade(nilai_akhir_mhs)
    mahasiswa.update(
        {"Mahasiswa"+str(i):{
            "nim":nim_mhs,
            "nilai_absen":nilai_absen_mhs,
            "nilai_tugas":nilai_tugas_mhs,
            "nilai_uts":nilai_uts_mhs,
            "nilai_uas":nilai_uas_mhs,
            "nilai_akhir":nilai_akhir_mhs,
            "nilai_grade":nilai_grade_mhs}
        }
    )
    total_nilai = total_nilai + nilai_akhir_mhs
    i = i+1

print('\n----------------------------------------------------')
print('Nim \t: 1811600350')
print('Nama \t: Bimo Asward Wibisono')
print('Kelas \t: XM')
print('Tugas \t: Data Sains')
print('Tugas \t: Input Data Mahasiswa')
print('----------------------------------------------------')

d=0
while d<jml_mhs:
    print("\n\nMahasiswa ke", d+1)
    print("Nim \t\t:", mahasiswa["Mahasiswa"+str(d)]["nim"])
    print("Nilai Absen \t:", mahasiswa["Mahasiswa"+str(d)]["nilai_absen"])
    print("Nilai Tugas \t:", mahasiswa["Mahasiswa"+str(d)]["nilai_tugas"])
    print("Nilai UTS \t:", mahasiswa["Mahasiswa"+str(d)]["nilai_uts"])
    print("Nilai UAS \t:", mahasiswa["Mahasiswa"+str(d)]["nilai_uas"])
    print("Nilai Akhir \t:", mahasiswa["Mahasiswa"+str(d)]["nilai_akhir"])
    print("Nilai Grade \t:", mahasiswa["Mahasiswa"+str(d)]["nilai_grade"])
    
    d = d+1

print('\nNilai rata-rata kelas : ', (total_nilai/len(mahasiswa)))