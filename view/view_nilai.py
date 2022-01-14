import os
import time
from ui.color import c
from ui.a_loading import load
from model._data import data

l = load()


class view:

    def tampil(self):
        os.system('clear')
        print('''
 +---------------------------------------------------+
 +---------{  PROGRAM INPUT DATA MAHASISWA  }--------+
 +---------------------------------------------------+
            \n''')
        l.loading()
        os.system('clear')
        if data.mahasiswa.items():
            print("=" * 61)
            print("|" + "\t" * 2 + "DAFTAR NILAI MAHASISWA" + "\t" * 3 +
                  "    |")
            print("=" * 61)
            print("|   \tNAMA\t   |\tNIM \t| TUGAS | UTS | UAS | AKHIR |")
            print("=" * 61)
            for tampil in data.mahasiswa.items():
                print("| {0:15}   | {1:9} | {2:5} | {3:3} | {4:3} | {5:5} |".
                      format(tampil[0], tampil[1][0], tampil[1][1],
                             tampil[1][2], tampil[1][3],
                             "%.2f" % float(tampil[1][4])))
                print("=" * 61)
            time.sleep(3)
            os.system('clear')
        else:
            os.system('clear')
            print('\n', c.REDBG, c.BLACK, '''DATA TIDAK DI TEMUKAN''', c.END)
            time.sleep(3)
            os.system('clear')

    def cari(self):
        os.system('clear')
        print('''
 +---------------------------------------------------+
 +---------{  PROGRAM INPUT  DATA MAHASISWA  }-------+
 +---------------------------------------------------+
            \n''')
        l.loading()
        os.system('clear')

        if self._nama in data.mahasiswa.keys():

            print("=" * 61)
            print("|" + "\t" * 2 + "DAFTAR NILAI MAHASISWA" + "\t" * 3 +
                  "    |")
            print("=" * 61)
            print("|   \tNAMA\t   |\tNIM \t| TUGAS | UTS | UAS | AKHIR |")
            print("=" * 61)

            print(
                "| {0:15}   | {1:9} | {2:5} | {3:3} | {4:3} | {5:5} |".format(
                    self._nama, self._nim, self._tugas, self._uts, self._uas,
                    "%.2f" % float(self._akhir)))
            print("=" * 61)

            time.sleep(3)
            os.system('clear')
        else:
            os.system('clear')
            print('\n', c.REDBG, c.BLACK, '''DATA TIDAK DI TEMUKAN''', c.END)
            time.sleep(3)
            os.system('clear')

    def falses(self):
        os.system('clear')
        print('\n', c.REDBG, c.BLACK, '''DATA TIDAK DI TEMUKAN''', c.END)
        time.sleep(3)
        os.system('clear')

    def false_menu(self):
        print('\t', c.REDBG, 'MENU TIDAK DI TEMUKAN!', c.END)

    def view_menu(self):

        print(
            c.VIOLET, '''
                                ┏┳┓┏━┓╻ ╻╻  ┏━┓┏┓╻┏━┓   ┏━┓┏━╸╺━┓┏━┓
                                ┃┃┃┣━┫┃ ┃┃  ┣━┫┃┗┫┣━┫   ┣┳┛┣╸ ┏━┛┣━┫
                                ╹ ╹╹ ╹┗━┛┗━╸╹ ╹╹ ╹╹ ╹   ╹┗╸┗━╸┗━╸╹ ╹
                                ────────────────────────────────────
                    ''', c.END)
        print(
            c.BLUE, '''
                +---------{  WELCOME TO PROGRAM INPUT DATA MAHASISWA  }--------+
                +--------------------------{  MENU  }--------------------------+
                    
                    ''', c.END)
        print('''
                { 1 } TAMBAH DATA
                { 2 } UBAH DATA
                { 3 } HAPUS DATA
                { 4 } CARI DATA
                { 5 } TAMPILKAN DATA
                    
                { e } EXIT
                
                
                    ''')

    def header(self):
        print('''
 +---------------------------------------------------+
 +---------{  PROGRAM INPUT DATA MAHASISWA  }--------+
 +---------------------------------------------------+
            \n''')

    def clean(self):
        os.system('clear')

    def exite(self):
        print('''
              ╺┳╸┏━╸┏━┓╻┏┳┓┏━┓   ╻┏ ┏━┓┏━┓╻╻ ╻
               ┃ ┣╸ ┣┳┛┃┃┃┃┣━┫   ┣┻┓┣━┫┗━┓┃┣━┫
               ╹ ┗━╸╹┗╸╹╹ ╹╹ ╹   ╹ ╹╹ ╹┗━┛╹╹ ╹
              ''')
        time.sleep(3)
        os.system('clear')
