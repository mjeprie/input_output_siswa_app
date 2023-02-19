import io_siswa
import os.path

def tampilkan_kelas(daftar_kelas):
    for index, kelas in enumerate(daftar_kelas):
        print(f"{index + 1}. {kelas}")


daftar_kelas = ['X IPA 1', 'X IPA 2', 'X IPS 1', 'X IPS 2']

for kelas in daftar_kelas:
    if not os.path.exists('data/' + kelas + '.txt'):
        with open('data/' + kelas + '.txt', 'w') as file:
            pass

while True:
    print('Absensi Siswa')
    print('-------------')
    print('Menu:')
    print("1. Tampilkan nama siswa")
    print("2. Edit nama siswa")
    print("3. Tambah siswa")
    print("4. Keluar")
    perintah = input("> ")

    match perintah:
        case '1':   # Tampilkan data siswa
            tampilkan_kelas(daftar_kelas)
            while True:
                kelas = int(input('> ')) - 1
                if kelas not in range(len(daftar_kelas)):
                    print('Pilihan tidak tepat.')
                    continue
                io_siswa.output_siswa(daftar_kelas[kelas])
                break

        case '2':   # Edit data siswa
            tampilkan_kelas(daftar_kelas)
            while True:
                kelas = int(input('> ')) - 1
                if kelas not in range(len(daftar_kelas)):
                    print('Pilihan tidak tepat.')
                    continue
                io_siswa.edit_siswa(daftar_kelas[kelas])
                break

        case '3':   # Tambah data siswa
            tampilkan_kelas(daftar_kelas)
            while True:
                kelas = int(input('> '))
                if kelas not in range(1, len(daftar_kelas) + 1):
                    print('Pilihan tidak tepat.')
                    continue
                io_siswa.input_siswa(kelas)
                break

        case '4':
            exit()
