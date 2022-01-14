import time
from ui.color import c
from view.view_nilai import view
from model.daftar_nilai import daftar

d = daftar()
p = view()
p.clean()
while True:
    p.view_menu()
    select_menu = input('\33[45m PILIH MENU \33[41m\33[30m ~# \33[0m ')
    if select_menu == '1':
        p.clean()
        p.header()
        d.tambah_data()
    elif select_menu == '2':
        p.clean()
        p.header()
        d.ubah_data()
    elif select_menu == '3':
        p.clean()
        p.header()
        d.hapus_data()
    elif select_menu == '4':
        p.clean()
        p.header()
        d.cari_data()
    elif select_menu == '5':
        p.clean()
        p.header()
        p.tampil()
    elif select_menu == 'e' or select_menu == 'E':
        p.clean()
        p.exite()
        exit()
    else:
        p.clean()
        p.view_menu()
        p.false_menu()
        time.sleep(3)
        p.clean()
