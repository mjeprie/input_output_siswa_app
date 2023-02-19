import PySimpleGUI as sg
import io_siswa
import os.path


def tampilkan_kelas(daftar_kelas):
    for index, kelas in enumerate(daftar_kelas):
        print(f"{index + 1}. {kelas}")


daftar_kelas = ['X IPA 1', 'X IPA 2', 'X IPS 1', 'X IPS 2']

for kelas in daftar_kelas:
    if not os.path.exists('data/' + kelas + '.txt'):
        with open('data/'+kelas+'.txt', 'w') as file:
            pass

sg.theme('Topanga')   # Add a touch of color
# All the stuff inside your window.

judul_label = sg.Text("Daftar Siswa")
daftar_kelas_listbox = sg.Combo(values=daftar_kelas, key='Daftar Kelas', readonly=True, enable_events=True, default_value=daftar_kelas[0])
tampilkan_siswa_button = sg.Button('Tampilkan')
nama_siswa_inputtext = sg.InputText(key='Nama Baru')
update_siswa_button = sg.Button('Update')
tambah_siswa_button = sg.Button('Tambah', button_color="white on green")
hapus_siswa_button = sg.Button('Hapus', button_color="white on red")
daftar_siswa_label = sg.Text('', key="Nama Kelas")
daftar_siswa_listbox = sg.Listbox(values=io_siswa.baca_data(daftar_kelas[0]), size=(50, 10), key='Daftar Nama Siswa', enable_events=True)
keluar_button = sg.Button('Keluar')


layout = [[judul_label, daftar_kelas_listbox],
          [nama_siswa_inputtext, update_siswa_button, tambah_siswa_button, hapus_siswa_button],
          [daftar_siswa_listbox],
          [keluar_button]]

# Create the Window
window = sg.Window("Daftar Siswa", layout)

while True:
    event, values = window.read()
    match event:
        case sg.WIN_CLOSED | 'Keluar':
            break
        case 'Daftar Kelas':
            print('update listbox')
            data_siswa = io_siswa.baca_data(values['Daftar Kelas'])
            window['Daftar Nama Siswa'].update(values=data_siswa)
            window['Nama Baru'].update(value='')
        case 'Update':
            if values['Nama Baru'] != '' and values['Daftar Nama Siswa'] != []:
                data_siswa = io_siswa.baca_data(values['Daftar Kelas'])
                data_siswa[data_siswa.index(values['Daftar Nama Siswa'][0])] = (values['Nama Baru'] + '\n').title()
                io_siswa.tulis_data(data_siswa, values['Daftar Kelas'])
                data_siswa = io_siswa.baca_data(values['Daftar Kelas'])
                window['Daftar Nama Siswa'].update(values=data_siswa)
                window['Nama Baru'].update(value='')
        case 'Tambah':
            if values['Nama Baru'] != '':
                data_siswa = io_siswa.baca_data(values['Daftar Kelas'])
                data_siswa.append(values['Nama Baru'] + '\n')
                io_siswa.tulis_data(data_siswa, values['Daftar Kelas'])
                data_siswa = io_siswa.baca_data(values['Daftar Kelas'])
                window['Daftar Nama Siswa'].update(values=data_siswa)
                window['Nama Baru'].update(value='')
        case 'Hapus':
            if values['Daftar Nama Siswa'] != []:
                data_siswa = io_siswa.baca_data(values['Daftar Kelas'])
                data_siswa.pop(data_siswa.index(values['Daftar Nama Siswa'][0]))
                io_siswa.tulis_data(data_siswa, values['Daftar Kelas'])
                window['Daftar Nama Siswa'].update(values=data_siswa)
        case 'Daftar Nama Siswa':
            if values['Daftar Kelas'] != '':
                window['Nama Baru'].update(value=values['Daftar Nama Siswa'][0].strip('\n'))

    print('e:', event, '| v:', values)

window.close()
