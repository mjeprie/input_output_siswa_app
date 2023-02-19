def baca_data(kelas):
    with open('data/' + kelas + '.txt', 'r') as file:
        data = file.readlines()
        return data

def tulis_data(data, kelas):
    data = list(set(data))
    with open('data/' + kelas + '.txt', 'w') as file:
        data.sort()
        file.writelines(data)

def input_siswa(kelas):
    kelas = kelas.upper()
    print(f"Input data {kelas}")
    print('----------')
    print("*Kosongkan untuk berhenti")
    data = baca_data(kelas)
    while True:
        nama = input('Nama: ').title()
        if nama == '':
            print("Input data selesai")
            break
        data.append(nama + '\n')
    tulis_data(data, kelas)

def output_siswa(kelas):
    kelas = kelas.upper()
    print(f"Absensi Kelas {kelas}")
    data = baca_data(kelas)
    if data == []:
        print('<--Kosong-->')
        return None
    for index, siswa in enumerate(data):
        siswa = siswa.strip('\n')
        print(f"{index+ 1 }. {siswa}")
    return data

def edit_siswa(kelas):
    data = output_siswa(kelas)
    no_siswa = int(input('Edit Siswa Nomor: '))
    nama = input('Nama: ').title()
    data[no_siswa - 1] = nama + '\n'
    tulis_data(data, kelas)