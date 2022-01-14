import time
from ui.color import c
from ui.a_loading import load
from view.view_nilai import view
from view.input_nilai import input_data
from model._data import data

l = load()
p = view()


class daftar:

    def tambah_data(self):
        input_data.data_input(self)
        data.mahasiswa[
            self.
            _nama] = self._nim, self._tugas, self._uts, self._uas, self._akhir

        p.clean()
        p.header()
        l.loading()
        p.clean()
        p.header()
        print('\n ', c.GREENBG, c.BLACK, 'DATA TELAH DI TAMBAHKAN!', c.END)
        time.sleep(3)
        p.clean()

    def ubah_data(self):
        print('+---{  MASUKAN NAMA DARI DATA YANG AKAN DI UBAH  }--+\n')
        input_data.nama_input(self)

        if self._nama in data.mahasiswa.keys():
            input_data.new_data(self)
            data.mahasiswa[
                self.
                _nama] = self._nim, self._tugas, self._uts, self._uas, self._akhir
            p.clean()
            p.header()
            l.loading()
            p.clean()
            p.header()
            print('\n ', c.BLUEBG, c.BLACK, 'DATA BERHASIL DI UBAH!', c.END)
            time.sleep(3)
            p.clean()
        else:
            p.falses()

    def hapus_data(self):
        print('+---{  MASUKAN NAMA DARI DATA YANG AKAN DIHAPUS  }--+\n')
        input_data.nama_input(self)

        if self._nama in data.mahasiswa:

            del data.mahasiswa[self._nama]
            p.clean()
            p.header()
            l.loading()
            p.clean()
            p.header()
            print('\n ', c.REDBG, c.BLACK, 'DATA BERHASIL DI HAPUS!', c.END)
            time.sleep(3)
            p.clean()
        else:
            p.falses()

    def cari_data(self):
        ('+---{  MASUKAN NAMA DARI DATA YANG AKAN DI CARI  }--+\n')
        input_data.nama_input(self)
        view.cari(self)
